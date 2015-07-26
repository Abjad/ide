# -*- encoding: utf-8 -*-
import datetime
import os
import time
from abjad.tools import stringtools
from ide.idetools.Wrangler import Wrangler


class PackageWrangler(Wrangler):
    r'''Package wrangler.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_mandatory_copy_target_storehouse',
        )

    ### INITIALIZER ###

    def __init__(self, session=None):
        from ide import idetools
        assert session is not None
        superclass = super(PackageWrangler, self)
        superclass.__init__(session=session)
        self._mandatory_copy_target_storehouse = None

    ### PRIVATE PROPERTIES ###

    @property
    def _command_to_method(self):
        superclass = super(PackageWrangler, self)
        result = superclass._command_to_method
        result = result.copy()
        result.update({
            '<': self.go_to_previous_package,
            '>': self.go_to_next_package,
            #
            'dc*': self.check_every_definition_py,
            'de*': self.edit_every_definition_py,
            #
            'ii*': self.interpret_every_illustration_ly,
            'io*': self.open_every_illustration_pdf,
            #
            'di*': self.illustrate_every_definition_py,  
            #
            'cp': self.copy_package,
            'new': self.make_package,
            'ren': self.rename_package,
            'rm': self.remove_packages,
            #
            'ck*': self.check_every_package,
            #
            'so*': self.open_every_score_pdf,
            })
        result.update(self._commands)
        return result

    ### PRIVATE METHODS ###

    def _is_valid_directory_entry(self, expr):
        superclass = super(PackageWrangler, self)
        if superclass._is_valid_directory_entry(expr):
            if '.' not in expr:
                return True
        return False

    def _list_metadata_py_files_in_all_directories(self):
        paths = []
        directories = self._list_all_directories_with_metadata_pys()
        for directory in directories:
            path = os.path.join(directory, '__metadata__.py')
            paths.append(path)
        paths.sort()
        return paths

    def _make_extra_commands_menu_section(self, menu):
        commands = []
        commands.extend(self._extra_commands)
        if commands:
            menu.make_command_section(
                is_hidden=True,
                commands=commands,
                name='extra commands',
                )

    def _make_basic_operations_menu_section(self, menu):
        commands = []
        commands.append(('copy', 'cp'))
        commands.append(('new', 'new'))
        commands.append(('rename', 'ren'))
        commands.append(('remove', 'rm'))
        menu.make_command_section(
            commands=commands,
            name='basic operations',
            )

    def _make_main_menu(self):
        superclass = super(PackageWrangler, self)
        menu = superclass._make_main_menu()
        self._make_extra_commands_menu_section(menu)
        self._make_basic_operations_menu_section(menu)
        return menu

    ### PUBLIC METHODS ###

    def check_every_definition_py(self):
        r'''Checks ``definition.py`` in every package.

        Returns none.
        '''
        managers = self._list_visible_asset_managers()
        inputs, outputs = [], []
        method_name = 'check_definition_py'
        for manager in managers:
            method = getattr(manager, method_name)
            inputs_, outputs_ = method(dry_run=True)
            inputs.extend(inputs_)
            outputs.extend(outputs_)
        messages = self._format_messaging(inputs, outputs, verb='check')
        self._io_manager._display(messages)
        result = self._io_manager._confirm()
        if self._session.is_backtracking or not result:
            return
        start_time = time.time()
        for manager in managers:
            method = getattr(manager, method_name)
            method()
        stop_time = time.time()
        total_time = stop_time - start_time
        total_time = int(total_time)
        message = 'total time: {} seconds.'
        message = message.format(total_time)
        self._io_manager._display(message)

    def check_every_package(
        self, 
        indent=0,
        problems_only=None, 
        supply_missing=None,
        ):
        r'''Checks every package.

        Returns none.
        '''
        messages = []
        missing_directories, missing_files = [], []
        supplied_directories, supplied_files = [], []
        tab = indent * self._io_manager._tab
        if problems_only is None:
            prompt = 'show problem assets only?'
            result = self._io_manager._confirm(prompt)
            if self._session.is_backtracking or result is None:
                return messages, missing_directories, missing_files
            problems_only = bool(result)
        managers = self._list_visible_asset_managers()
        found_problem = False
        for manager in managers:
            with self._io_manager._silent():
                result = manager.check_package(
                    return_messages=True,
                    problems_only=problems_only,
                    )
            messages_, missing_directories_, missing_files_ = result
            missing_directories.extend(missing_directories_)
            missing_files.extend(missing_files_)
            messages_ = [stringtools.capitalize_start(_) for _ in messages_]
            messages_ = [tab + _ for _ in messages_]
            if messages_:
                found_problem = True
                messages.extend(messages_)
            else:
                message = 'No problem assets found.'
                message = tab + tab + message
                messages.append(message)
        found_problems = bool(messages)
        if self._session.is_in_score:
            path = self._get_current_directory()
            name = os.path.basename(path)
            count = len(managers)
            message = '{} directory ({} packages):'.format(name, count)
            if not found_problems:
                message = '{} OK'.format(message)
            messages.insert(0, message)
        self._io_manager._display(messages)
        if not found_problem:
            return messages, missing_directories, missing_files
        if supply_missing is None:
            prompt = 'supply missing directories and files?'
            result = self._io_manager._confirm(prompt)
            if self._session.is_backtracking or result is None:
                return messages, missing_directories, missing_files
            supply_missing = bool(result)
        if not supply_missing:
            return messages, missing_directories, missing_files
        messages = []
        for manager in managers:
            with self._io_manager._silent():
                result = manager.check_package(
                    return_supply_messages=True,
                    supply_missing=True,
                    )
            messages_, supplied_directories_, supplied_files_ = result
            supplied_directories.extend(supplied_directories_)
            supplied_files.extend(supplied_files_)
            if messages_:
                messages_ = [tab + tab + _ for _ in messages_]
                messages.extend(messages_)
        self._io_manager._display(messages)
        return messages, supplied_directories, supplied_files

    def copy_package(self):
        r'''Copies package.

        Returns none.
        '''
        self._copy_asset(
            new_storehouse=self._mandatory_copy_target_storehouse,
            )

    def edit_every_definition_py(self):
        r'''Opens ``definition.py`` in every package.

        Returns none.
        '''
        self._open_in_every_package('definition.py')

    def edit_every_metadata_py(self):
        r'''Edits ``__metadata__.py`` in every package.

        Returns none.
        '''
        paths = self._list_metadata_py_files_in_all_directories()
        messages = []
        messages.append('will open ...')
        for path in paths:
            message = '    ' + path
            messages.append(message)
        self._io_manager._display(messages)
        result = self._io_manager._confirm()
        if self._session.is_backtracking or not result:
            return
        self._io_manager.open_file(paths)

    def go_to_next_package(self):
        r'''Goes to next package.

        Returns none.
        '''
        self._go_to_next_package()

    def go_to_previous_package(self):
        r'''Goes to previous package.

        Returns none.
        '''
        self._go_to_previous_package()

    def illustrate_every_definition_py(self):
        r'''Illustrates ``definition.py`` in every package.

        Returns none.
        '''
        managers = self._list_visible_asset_managers()
        inputs, outputs = [], []
        method_name = 'illustrate_definition_py'
        for manager in managers:
            method = getattr(manager, method_name)
            inputs_, outputs_ = method(dry_run=True)
            inputs.extend(inputs_)
            outputs.extend(outputs_)
        messages = self._format_messaging(inputs, outputs, verb='illustrate')
        self._io_manager._display(messages)
        result = self._io_manager._confirm()
        if self._session.is_backtracking or not result:
            return
        for manager in managers:
            method = getattr(manager, method_name)
            method()

    def interpret_every_illustration_ly(
        self, 
        open_every_illustration_pdf=True,
        ):
        r'''Interprets ``illustration.ly`` in every package.

        Makes ``illustration.pdf`` in every package.

        Returns none.
        '''
        managers = self._list_visible_asset_managers()
        inputs, outputs = [], []
        method_name = 'interpret_illustration_ly'
        for manager in managers:
            method = getattr(manager, method_name)
            inputs_, outputs_ = method(dry_run=True)
            inputs.extend(inputs_)
            outputs.extend(outputs_)
        messages = self._format_messaging(inputs, outputs)
        self._io_manager._display(messages)
        result = self._io_manager._confirm()
        if self._session.is_backtracking or not result:
            return
        for manager in managers:
            with self._io_manager._silent():
                method = getattr(manager, method_name)
                subprocess_messages, candidate_messages = method()
            if subprocess_messages:
                self._io_manager._display(subprocess_messages)
                self._io_manager._display(candidate_messages)
                self._io_manager._display('')
                
    def list_every_metadata_py(self):
        r'''Lists ``__metadata__.py`` in every package.

        Returns none.
        '''
        directories = self._list_all_directories_with_metadata_pys()
        paths = [os.path.join(_, '__metadata__.py') for _ in directories]
        messages = paths[:]
        self._io_manager._display(messages)
        message = '{} __metadata__.py files found.'
        message = message.format(len(paths))
        self._io_manager._display(message)

    def make_package(self):
        r'''Makes package.

        Returns none.
        '''
        if self._session.is_in_score:
            storehouse_path = self._current_storehouse_path
        else:
            example_score_packages = self._session.is_test
            storehouse_path = self._select_storehouse_path(
                example_score_packages=example_score_packages,
                )
            if self._session.is_backtracking or storehouse_path is None:
                return
        path = self._get_available_path(storehouse_path=storehouse_path)
        if self._session.is_backtracking or not path:
            return
        message = 'path will be {}.'.format(path)
        self._io_manager._display(message)
        result = self._io_manager._confirm()
        if self._session.is_backtracking or not result:
            return
        manager = self._get_manager(path)
        manager._make_package()
        paths = self._list_visible_asset_paths()
        if path not in paths:
            with self._io_manager._silent():
                self._clear_view()
        manager._run()

    def make_score_package(self):
        r'''Makes score package.

        Returns none.
        '''
        message = 'enter title'
        getter = self._io_manager._make_getter()
        getter.append_string(message)
        title = getter._run()
        if self._session.is_backtracking or not title:
            return
        package_name = stringtools.strip_diacritics(title)
        package_name = stringtools.to_snake_case(package_name)
        confirmed = False 
        while not confirmed:
            package_path = os.path.join(
                self._configuration.user_score_packages_directory,
                package_name,
                )
            message = 'path will be {}.'.format(package_path)
            self._io_manager._display(message)
            result = self._io_manager._confirm()
            if self._session.is_backtracking:
                return
            confirmed = result
            if confirmed:
                break
            message = 'enter package name'
            getter = self._io_manager._make_getter()
            getter.append_string(message)
            package_name = getter._run()
            if self._session.is_backtracking or not package_name:
                return
            package_name = stringtools.strip_diacritics(package_name)
            package_name = stringtools.to_snake_case(package_name)
        manager = self._get_manager(package_path)
        manager._make_package()
        manager._add_metadatum('title', title)
        year = datetime.date.today().year
        manager._add_metadatum('year', year)
        package_paths = self._list_visible_asset_paths()
        if package_path not in package_paths:
            with self._io_manager._silent():
                self._clear_view()
        manager._run()

    def open_every_illustration_pdf(self):
        r'''Opens ``illustration.pdf`` in every package.

        Returns none.
        '''
        self._open_in_every_package('illustration.pdf')

    def open_every_score_pdf(self):
        r'''Opens ``score.pdf`` in every package.

        Returns none.
        '''
        managers = self._list_visible_asset_managers()
        paths = []
        for manager in managers:
            inputs, outputs = manager.open_score_pdf(dry_run=True)
            paths.extend(inputs)
        messages = ['will open ...']
        tab = self._io_manager._tab
        paths = [tab + _ for _ in paths]
        messages.extend(paths)
        self._io_manager._display(messages)
        result = self._io_manager._confirm()
        if self._session.is_backtracking or not result:
            return
        if paths:
            self._io_manager.open_file(paths)

    def remove_packages(self):
        r'''Removes one or more packages.
        
        Returns none.
        '''
        self._remove_assets()

    def rename_package(self):
        r'''Renames package.

        Returns none.
        '''
        self._rename_asset()

    def write_every_metadata_py(self):
        r'''Writes ``__metadata__.py`` in every package.

        Returns none.
        '''
        directories = self._list_all_directories_with_metadata_pys()
        managers = []
        for directory in directories:
            manager = self._io_manager._make_package_manager(directory)
            managers.append(manager)
        inputs, outputs = [], []
        method_name = 'write_metadata_py'
        for manager in managers:
            method = getattr(manager, method_name)
            inputs_, outputs_ = method(dry_run=True)
            inputs.extend(inputs_)
            outputs.extend(outputs_)
        messages = self._format_messaging(
            inputs, 
            outputs, 
            verb='write',
            )
        self._io_manager._display(messages)
        result = self._io_manager._confirm()
        if self._session.is_backtracking or not result:
            return
        with self._io_manager._silent():
            for manager in managers:
                method = getattr(manager, method_name)
                method()
        message = '{} __metadata__.py files rewritten.'
        message = message.format(len(managers))
        self._io_manager._display(message)