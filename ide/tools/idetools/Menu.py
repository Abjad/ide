# -*- encoding: utf-8 -*-
import os
import re
import shlex
from abjad.tools import sequencetools
from abjad.tools import stringtools
from ide.tools.idetools.Controller import Controller


class Menu(Controller):
    r'''Menu.

    ..  container:: example

        ::

            >>> session = ide.tools.idetools.Session()
            >>> menu = ide.tools.idetools.Menu(session=session)

        ::

            >>> commands = []
            >>> commands.append(('foo - add', 'add'))
            >>> commands.append(('foo - delete', 'delete'))
            >>> commands.append(('foo - modify', 'modify'))
            >>> section = menu.make_command_section(
            ...     commands=commands,
            ...     name='test',
            ...     )

        ::

            >>> menu
            <Menu (1)>

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_asset_section',
        '_menu_sections',
        '_name',
        '_subtitle',
        '_title',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        name=None,
        session=None,
        subtitle=None,
        title=None,
        ):
        Controller.__init__(self, session=session)
        self._menu_sections = []
        self._name = name
        self._subtitle = subtitle
        self._title = title

    ### SPECIAL METHODS ###

    def __getitem__(self, expr):
        r'''Gets menu section indexed by `expr`.

        Returns menu section with name equal to `expr` when `expr` is a string.

        Returns menu section at index `expr` when `expr` is an integer.
        '''
        if isinstance(expr, str):
            for section in self.menu_sections:
                if section.name == expr:
                    return section
            raise KeyError(expr)
        else:
            return self.menu_sections.__getitem__(expr)

    def __len__(self):
        r'''Gets number of menu sections in menu.

        Returns nonnegative integer.
        '''
        return len(self.menu_sections)

    def __repr__(self):
        r'''Gets interpreter representation of menu.

        Returns string.
        '''
        if self.name:
            string = '<{} {!r} ({})>'
            string = string.format(type(self).__name__, self.name, len(self))
        else:
            string = '<{} ({})>'
            string = string.format(type(self).__name__, len(self))
        return string

    ### PRIVATE METHODS ###

    def _change_input_to_directive(self, input_):
        r'''Match order:
        
            1. all command sections
            2. 'assets' section, if it exists
            3. 'material summary', if it exists
            4. aliases, if any are defined

        This avoids file name new-stylesheet.ily aliasing the (new) command.
        '''
        input_ = stringtools.strip_diacritics(input_)
        if input_ == '!':
            return
        if input_.startswith('!'):
            if self._has_shell_command():
                return input_
            else:
                return
        ends_with_bang = input_.endswith('!')
        if ends_with_bang and input_[:-1] == 'q':
            self._session._clear_terminal_after_quit = True
        input_ = input_.strip('!')
        if self._user_enters_nothing(input_):
            default_value = None
            for section in self.menu_sections:
                if section._has_default_value:
                    default_value = section._default_value
            if default_value is not None:
                return self._enclose_in_list(default_value)
        elif input_ in ('h', 'q', 'b', '<return>'):
            self._session._pending_redraw = True
            return input_
        elif input_ == '?' and self._has_display_action_commands_command():
            self._session._pending_redraw = True
            return input_
        elif input_ == ';' and self._has_display_navigation_commands_command():
            self._session._pending_redraw = True
            return input_
        elif input_ == 's' and self._session.is_in_score:
            self._session._pending_redraw = True
            return input_
        # match on exact case
        asset_section = None
        for section in self.menu_sections:
            if section.is_asset_section:
                asset_section = section
                continue
            for menu_entry in section:
                if menu_entry.matches(input_):
                    return_value = menu_entry.return_value
                    if ends_with_bang:
                        return_value = return_value + '!'
                    return self._enclose_in_list(return_value)
        if asset_section is not None:
            for menu_entry in asset_section:
                if menu_entry.matches(input_):
                    return_value = menu_entry.return_value
                    if ends_with_bang:
                        return_value = return_value + '!'
                    return self._enclose_in_list(return_value)
        # lower case version of the two sections above
        asset_section = None
        for section in self.menu_sections:
            if section.is_asset_section:
                asset_section = section
                continue
            for menu_entry in section:
                if menu_entry.matches(input_.lower()):
                    return_value = menu_entry.return_value
                    if ends_with_bang:
                        return_value = return_value + '!'
                    return self._enclose_in_list(return_value)
        if asset_section is not None:
            for menu_entry in asset_section:
                #if menu_entry.matches(input_):
                if menu_entry.matches(input_.lower()):
                    return_value = menu_entry.return_value
                    if ends_with_bang:
                        return_value = return_value + '!'
                    return self._enclose_in_list(return_value)
        if self._user_enters_argument_range(input_):
            return self._handle_argument_range_input(input_)
        current_score_directory = self._session.current_score_directory
        aliased_path = self._session.aliases.get(input_, None)
        if current_score_directory and aliased_path:
            aliased_path = os.path.join(current_score_directory, aliased_path)
            if os.path.isfile(aliased_path):
                self._io_manager.open_file(aliased_path)
            else:
                message = 'file does not exist: {}.'
                message = message.format(aliased_path)
                self._io_manager._display(message)
            return 'user entered alias'

    def _enclose_in_list(self, expr):
        if self._has_ranged_section():
            return [expr]
        else:
            return expr

    def _get_first_nonhidden_return_value_in_menu(self):
        for section in self.menu_sections:
            if section.is_hidden:
                continue
            if section._menu_entry_return_values:
                return section._menu_entry_return_values[0]

    def _group_by_annotation(self, lines):
        new_lines = []
        current_annotation = ''
        pattern = re.compile('(.*)(\s+)\((.+)\)')
        tab = self._io_manager._tab
        for line in lines:
            line = line.replace('', '')
            match = pattern.match(line)
            if match:
                display_string, _, annotation = match.groups()
                if not annotation == current_annotation:
                    current_annotation = annotation
                    new_line = '{}{}:'.format(tab, current_annotation)
                    new_lines.append(new_line)
                new_line = tab + display_string
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        return new_lines

    def _handle_argument_range_input(self, input_):
        if not self._has_ranged_section():
            return
        for section in self.menu_sections:
            if section.is_ranged:
                ranged_section = section
        entry_numbers = ranged_section._argument_range_string_to_numbers(
            input_)
        if not entry_numbers:
            return
        entry_indices = [entry_number - 1 for entry_number in entry_numbers]
        result = []
        for i in entry_indices:
            entry = ranged_section._menu_entry_return_values[i]
            result.append(entry)
        return result

    def _handle_user_input(self):
        input_ = self._io_manager._handle_input(
            '', 
            prompt_character=self.prompt_character,
            )
        user_entered_lone_return = input_ == ''
        directive = None
        parts = shlex.split(input_, posix=False)
        length = len(parts)
        for i in range(len(parts)):
            count = length - i
            candidate = ' '.join(parts[:count])
            directive = self._change_input_to_directive(candidate)
            if directive == 'user entered alias':
                continue
            if directive is not None:
                if count < length:
                    remaining_count = length - count
                    remaining_parts = parts[-remaining_count:]
                    glued_remaining_parts = []
                    for remaining_part in remaining_parts:
                        remaining_part = remaining_part.replace(' ', '~')
                        glued_remaining_parts.append(remaining_part)
                    remaining_input = ' '.join(glued_remaining_parts)
                    pending_input = self._session._pending_input or ''
                    pending_input = pending_input + remaining_input
                    self._session._pending_input = pending_input
                    self._session._pending_redraw = True
                break
        if directive == 'user entered alias':
            return
        directive = self._strip_default_notice_from_strings(directive)
        if directive is None and user_entered_lone_return:
            result = '<return>'
        elif directive is None and not user_entered_lone_return:
            message = 'unknown command: {!r}.'
            message = message.format(input_)
            self._io_manager._display([message, ''])
            result = None
            if (self._session.is_test and 
                not self._session._allow_unknown_command_during_test):
                message = 'tests should contain no unknown commands.'
                raise Exception(message)
        else:
            result = directive
        return result

    def _has_display_action_commands_command(self):
        for section in self.menu_sections:
            for entry in section.menu_entries:
                if entry.key == '?':
                    return True
        return False

    def _has_display_navigation_commands_command(self):
        for section in self.menu_sections:
            for entry in section.menu_entries:
                if entry.key == ';':
                    return True
        return False

    def _has_numbered_section(self):
        return any(x.is_numbered for x in self.menu_sections)

    def _has_ranged_section(self):
        return any(x.is_ranged for x in self.menu_sections)

    def _has_shell_command(self):
        for section in self.menu_sections:
            for entry in section.menu_entries:
                if entry.key == '!':
                    return True
        return False

    def _is_recognized_input(self, expr):
        if isinstance(expr, str):
            if expr in self._command_name_to_method:
                return True
            if (expr.endswith('!') and
                expr[:-1] in self._command_name_to_method):
                return True
        return False

    @staticmethod
    def _ljust(string, width):
        start_width = len(stringtools.strip_diacritics(string))
        if start_width < width:
            needed = width - start_width
            suffix = needed * ' '
            result = string + suffix
        else:
            result = string
        return result

    def _make_asset_lines(self):
        has_asset_section = False
        for section in self:
            if section.is_asset_section:
                has_asset_section = True
                break
        if not has_asset_section:
            return []
        assert section.is_asset_section
        lines = section._make_lines()
        if section.group_by_annotation:
            lines = self._group_by_annotation(lines)
        lines = self._make_bicolumnar(lines, strip=False)
        return lines

    def _make_action_command_section_lines(self):
        lines = []
        for section in self.menu_sections:
            found_one = False
            if not section.is_command_section:
                continue
            for menu_entry in section:
                if menu_entry.is_navigation:
                    continue
                found_one = True
                key = menu_entry.key
                display_string = menu_entry.display_string
                menu_line = self._io_manager._tab
                menu_line += '{} ({})'.format(display_string, key)
                lines.append(menu_line)
            if found_one:
                lines.append('')
        if lines:
            lines.pop()
        lines = self._make_bicolumnar(
            lines, 
            break_only_at_blank_lines=True,
            )
        title = self._session.menu_header
        title = title + ' - action commands'
        title = stringtools.capitalize_start(title)
        lines[0:0] = [title, '']
        lines.append('')
        return lines

    def _make_navigation_command_section_lines(self):
        lines = []
        for section in self.menu_sections:
            found_one = False
            if not section.is_command_section:
                continue
            for menu_entry in section:
                if not menu_entry.is_navigation:
                    continue
                found_one = True
                key = menu_entry.key
                display_string = menu_entry.display_string
                menu_line = self._io_manager._tab
                menu_line += '{} ({})'.format(display_string, key)
                lines.append(menu_line)
            if found_one:
                lines.append('')
        if lines:
            lines.pop()
        lines = self._make_bicolumnar(
            lines, 
            break_only_at_blank_lines=True,
            )
        title = self._session.menu_header
        title = title + ' - view & navigation commands'
        title = stringtools.capitalize_start(title)
        lines[0:0] = [title, '']
        lines.append('')
        return lines

    def _make_bicolumnar(
        self, 
        lines, 
        break_only_at_blank_lines=False,
        strip=True,
        ):
        # http://stackoverflow.com/questions/566746/
        # how-to-get-console-window-width-in-python
        result = os.popen('stty size', 'r').read().split()
        if result:
            terminal_height, terminal_width = result
            terminal_height = int(terminal_height)
            terminal_width = int(terminal_width)
        # returns none when run under py.test
        else:
            terminal_height, terminal_width = 24, 80
        if terminal_width <= 80:
            return lines
        if len(lines) < terminal_height - 8:
            return lines
        if strip:
            lines = [_.strip() for _ in lines]
        all_packages_lines = [_ for _ in lines if _.startswith('all')]
        lines = [_ for _ in lines if not _.startswith('all')]
        # remove consecutive blank lines from comprehension above
        clean_lines = []
        for line in lines:
            if line == '':
                if clean_lines and clean_lines[-1] == '':
                    continue
            clean_lines.append(line)
        # remove initial blank line
        if clean_lines[0] == '':
            clean_lines.pop(0)
        lines = clean_lines
        midpoint = int(len(lines)/2)
        if break_only_at_blank_lines:
            while lines[midpoint] != '':
                midpoint += 1
            assert lines[midpoint] == ''
        left_lines = lines[:midpoint]
        if break_only_at_blank_lines:
            right_lines = lines[midpoint+1:]
            assert len(left_lines) + len(right_lines) == len(lines) - 1
        else:
            right_lines = lines[midpoint:]
        left_count, right_count = len(left_lines), len(right_lines)
        #assert right_count <= left_count, repr((left_count, right_count))
        if strip:
            left_width = max(len(_.strip()) for _ in left_lines)
            right_width = max(len(_.strip()) for _ in right_lines)
        else:
            left_width = max(len(_) for _ in left_lines)
            right_width = max(len(_) for _ in right_lines)
        left_lines = [self._ljust(_, left_width) for _ in left_lines]
        right_lines = [self._ljust(_, right_width) for _ in right_lines]
        if strip:
            left_margin_width, gutter_width = 4, 4 
        else:
            left_margin_width, gutter_width = 0, 4 
        left_margin = left_margin_width * ' '
        gutter = gutter_width * ' '
        conjoined_lines = []
        for _ in sequencetools.zip_sequences(
            [left_lines, right_lines],
            truncate=False,
            ):
            if len(_) == 1:
                left_line = _[0]
                conjoined_line = left_margin + left_line
            elif len(_) == 2:
                left_line, right_line = _
                conjoined_line = left_margin + left_line + gutter + right_line
            conjoined_lines.append(conjoined_line)
        if all_packages_lines:
            blank_line = left_margin
            conjoined_lines.append(blank_line)
        for line in all_packages_lines:
            conjoined_line = left_margin + line
            conjoined_lines.append(conjoined_line)
        return conjoined_lines

    def _make_command_section_lines(self):
        result = []
        section_names = []
        for section in self.menu_sections:
            # TODO: check for duplicate section names at initialization
            if section.name in section_names:
                message = '{!r} contains duplicate {!r}.'
                message = message.format(self, section)
                raise Exception(message)
            else:
                section_names.append(section.name)
            hide = (not self._session.display_action_commands or
                not self._session.display_navigation_commands)
            if hide and section.is_hidden:
                continue
            if section.is_asset_section:
                continue
            if section.name == 'material summary':
                continue
            section_menu_lines = section._make_lines()
            result.extend(section_menu_lines)
        return result

    def _make_material_summary_lines(self):
        try:
            section = self['material summary']
        except KeyError:
            return []
        lines = section._make_lines()
        return lines

    def _make_section(
        self,
        default_index=None,
        display_prepopulated_values=False,
        group_by_annotation=True,
        is_asset_section=False,
        is_command_section=False,
        is_hidden=False,
        is_numbered=False,
        is_ranged=False,
        match_on_display_string=True,
        menu_entries=None,
        name=None,
        return_value_attribute='display_string',
        title=None,
        ):
        from ide.tools import idetools
        assert not (is_numbered and self._has_numbered_section())
        assert not (is_ranged and self._has_ranged_section())
        section = idetools.MenuSection(
            default_index=default_index,
            display_prepopulated_values=display_prepopulated_values,
            group_by_annotation=group_by_annotation,
            is_asset_section=is_asset_section,
            is_command_section=is_command_section,
            is_hidden=is_hidden,
            is_numbered=is_numbered,
            is_ranged=is_ranged,
            match_on_display_string=match_on_display_string,
            menu_entries=menu_entries,
            name=name,
            return_value_attribute=return_value_attribute,
            title=title,
            )
        self.menu_sections.append(section)
        self.menu_sections.sort(key=lambda x: x.name)
        noncommand_sections = [
            x for x in self.menu_sections
            if not x.is_command_section
            ]
        for noncommand_section in noncommand_sections:
            self.menu_sections.remove(noncommand_section)
        for noncommand_section in noncommand_sections:
            self.menu_sections.insert(0, noncommand_section)
        return section

    def _make_title_lines(self):
        result = []
        if self.title is not None:
            title = self.title
        else:
            title = self._session.menu_header
        result.append(stringtools.capitalize_start(title))
        if self.subtitle is not None:
            line = '  ' + self.subtitle
            result.append('')
            result.append(line)
        result.append('')
        return result

    def _make_visible_section_lines(self):
        lines = []
        lines.extend(self._make_title_lines())
        lines.extend(self._make_material_summary_lines())
        lines.extend(self._make_asset_lines())
        if lines and not all(_ == ' ' for _ in lines[-1]):
            lines.append('')
        lines.extend(self._make_command_section_lines())
        return lines

    def _redraw(self):
        self._session._pending_redraw = False
        self._io_manager.clear_terminal()
        if self._session.display_action_commands:
            lines = self._make_action_command_section_lines()
        elif self._session.display_navigation_commands:
            lines = self._make_navigation_command_section_lines()
        else:
            lines = self._make_visible_section_lines()
        self._io_manager._display(lines, capitalize=False, is_menu=True)

    def _return_value_to_location_pair(self, return_value):
        for i, section in enumerate(self.menu_sections):
            if return_value in section._menu_entry_return_values:
                j = section._menu_entry_return_values.index(return_value)
                return i, j

    def _run(self):
        with self._io_manager._controller(controller=self):
            while True:
                if self._session.pending_redraw:
                    self._redraw()
                    message = self._session._after_redraw_message
                    if message:
                        self._io_manager._display(message)
                        self._session._after_redraw_message = None
                result = None
                if not result:
                    result = self._handle_user_input()
                if self._session.is_quitting:
                    return result
                elif result == '<return>':
                    self._session._pending_redraw = True
                elif self._is_recognized_input(result):
                    self._command_name_to_method[result]()
                    return
                else:
                    return result

    @staticmethod
    def _strip_default_notice_from_strings(expr):
        if isinstance(expr, list):
            cleaned_list = []
            for element in expr:
                if element.endswith(' (default)'):
                    element = element.replace(' (default)', '')
                cleaned_list.append(element)
            return cleaned_list
        elif isinstance(expr, str):
            if expr.endswith(' (default)'):
                expr = expr.replace(' (default)', '')
            return expr
        else:
            return expr

    @staticmethod
    def _user_enters_argument_range(input_):
        if ',' in input_:
            return True
        if '-' in input_:
            return True
        return False

    @staticmethod
    def _user_enters_nothing(input_):
        return (
            not input_ or 
            (3 <= len(input_) and '<return>'.startswith(input_))
            )

    ### PUBLIC PROPERTIES ###

    @property
    def menu_sections(self):
        r'''Gets menu sections.

        Returns list.
        '''
        return self._menu_sections

    @property
    def name(self):
        r'''Gets name.

        Returns string.
        '''
        return self._name

    @property
    def prompt_character(self):
        r'''Gets prompt character.

        Returns '>'.
        '''
        return '>'

    @property
    def subtitle(self):
        r'''Gets subtitle.

        Returns string or none.
        '''
        return self._subtitle

    @property
    def title(self):
        r'''Gets title.

        Returns string or none.
        '''
        return self._title

    ### PUBLIC METHODS ###

    def make_asset_section(
        self,
        menu_entries=None,
        name='assets',
        ):
        r'''Makes asset section.

        With these attributes:

            * is asset section
            * is numbered
            * return value set to explicit

        Returns menu section.
        '''
        section = self._make_section(
            is_asset_section=True,
            is_numbered=True,
            menu_entries=menu_entries,
            name=name,
            return_value_attribute='explicit',
            )
        self._asset_section = section
        return section

    def make_command_section(
        self,
        is_hidden=False,
        default_index=None,
        match_on_display_string=False,
        commands=None,
        name=None,
        ):
        r'''Makes command section.

        Menu section with these attributes:

            * is command section
            * is not hidden
            * does NOT match on display string
            * return value attribute equal to ``'key'``

        Returns menu section.
        '''
        section = self._make_section(
            default_index=default_index,
            group_by_annotation=False,
            is_command_section=True,
            is_hidden=is_hidden,
            match_on_display_string=match_on_display_string,
            menu_entries=commands,
            name=name,
            return_value_attribute='key',
            )
        return section