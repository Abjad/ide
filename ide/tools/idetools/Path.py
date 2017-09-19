import abjad
import os
import pathlib
from ide.tools.idetools.Configuration import Configuration


class Path(abjad.Path):
    r'''Path.
    '''

    ### CLASS VARIABLES ###

    address_characters = ('@', '#', '%', '^', '*')

    configuration = Configuration()

    test_score_names = (
        'blue_score',
        'red_score',
        )

    ### CONSTRUCTOR ###

    def __new__(class_, argument, scores=None):
        if isinstance(argument, pathlib.Path) or os.sep in argument:
            self = pathlib.Path.__new__(class_, argument)
        else:
            arguments = []
            if argument in Path.test_score_names:
                arguments.append(Path.configuration.test_scores_directory)
                arguments.extend(2 * [argument])
            elif argument == 'boilerplate':
                arguments.append(
                    abjad.abjad_configuration.boilerplate_directory)
            elif argument == 'test_scores':
                arguments.append(Path.configuration.test_scores_directory)
            elif scores is not None:
                arguments.append(scores)
                arguments.extend(2 * [argument])
            else:
                arguments.append(
                    abjad.abjad_configuration.composer_scores_directory)
                arguments.extend(2 * [argument])
            self = pathlib.Path.__new__(class_, *arguments)
        if scores is not None:
            scores = type(self)(scores)
        self._scores = scores
        return self

    ### PRIVATE METHODS ###

    def _get_added_asset_paths(self):
        paths = []
        git_status_lines = self._get_git_status_lines()
        for line in git_status_lines:
            line = str(line)
            if line.startswith('A'):
                path = line.strip('A')
                path = path.strip()
                root = self.wrapper
                path = root / path
                paths.append(path)
        return paths

    def _get_git_status_lines(self):
        with abjad.TemporaryDirectoryChange(directory=self.wrapper):
            command = f'git status --porcelain {self}'
            return abjad.IOManager.run_command(command)

    def _get_repository_root(self):
        if not self.exists():
            return
        if self.wrapper is None:
            path = self
        else:
            path = self.wrapper
        test_scores = self.configuration.test_scores_directory
        if str(self).startswith(str(test_scores)):
            return self.wrapper
        while str(path) != str(path.parts[0]):
            for path_ in path.iterdir():
                if path_.name == '.git':
                    return type(self)(path)
            path = path.parent

    def _get_unadded_asset_paths(self):
        assert self.is_dir()
        paths = []
        root = self.wrapper
        git_status_lines = self._get_git_status_lines()
        for line in git_status_lines:
            line = str(line)
            if line.startswith('?'):
                path = line.strip('?')
                path = path.strip()
                path = root / path
                paths.append(path)
            elif line.startswith('M'):
                path = line.strip('M')
                path = path.strip()
                path = root / path
                paths.append(path)
        paths = [_ for _ in paths]
        return paths

    def _has_pending_commit(self):
        assert self.is_dir()
        command = f'git status {self}'
        with abjad.TemporaryDirectoryChange(directory=self):
            lines = abjad.IOManager.run_command(command)
        clean_lines = []
        for line in lines:
            line = str(line)
            clean_line = line.strip()
            clean_line = clean_line.replace(str(self), '')
            clean_lines.append(clean_line)
        for line in clean_lines:
            if 'Changes not staged for commit:' in line:
                return True
            if 'Changes to be committed:' in line:
                return True
        
    def _is_git_unknown(self):
        if not self.exists():
            return False
        git_status_lines = self._get_git_status_lines()
        git_status_lines = git_status_lines or ['']
        first_line = git_status_lines[0]
        if first_line.startswith('?'):
            return True
        return False

    def _unadd_added_assets(self):
        paths = []
        paths.extend(self._get_added_asset_paths())
        paths.extend(self._get_modified_asset_paths())
        commands = []
        for path in paths:
            command = f'git reset -- {path}'
            commands.append(command)
        command = ' && '.join(commands)
        with abjad.TemporaryDirectoryChange(directory=path):
            abjad.IOManager.spawn_subprocess(command)

    ### PUBLIC PROPERTIES ###

    @property
    def scores(self):
        r'''Gets scores directory.

        ..  container:: example

            ::

                >>> path = ide.Path(
                ...     '/path/to/scores/my_score/my_score',
                ...     scores='/path/to/scores',
                ...     )
                >>> path.scores
                Path*('/path/to/scores')

        Returns package path or none.
        '''
        if getattr(self, '_scores', None) is not None:
            result = self._scores
            result._scores = self._scores
            return result
        for scores in (
            self.configuration.test_scores_directory,
            abjad.abjad_configuration.composer_scores_directory,
            ):
            if str(self).startswith(str(scores)):
                return type(self)(scores)

    ### PUBLIC METHODS ###

    def get_header(self):
        r'''Gets menu header.

        Returns string.
        '''
        if self.is_external():
            if self.parent.name == abjad.abjad_configuration.composer_library:
                header = 'Abjad IDE : library'
            else:
                header = f'Abjad IDE : {self}'
            if not self.list_paths():
                header += ' (empty)'
            return header
        if self.is_scores():
            return 'Abjad IDE : scores'
        parts = [self.contents.get_title()]
        if self.is_wrapper():
            parts.append('wrapper')
        elif not self.is_contents():
            parts.extend(self.relative_to(self.contents).parts[:-1])
            parts.append(self.get_identifier())
        if parts and not self.list_paths():
            parts[-1] += ' (empty)'
        return ' : '.join(parts)

    def is_external(self):
        r'''Is true when path does not have form of score package path.

        ..  container:: example

            ::

                >>> path = ide.Path('/path/to/location')
                >>> path.is_external()
                True

        Returns true or false.
        '''
        if not self.name[0].isalpha() and not self.name == '_segments':
            return True
        for scores in (abjad.abjad_configuration.composer_scores_directory,
            self.configuration.test_scores_directory,
            getattr(self, '_scores', None),
            ):
            if str(self).startswith(str(scores)):
                return False
        return True

    def match_package_path(self, pattern, all=False):
        r'''Matches package path against `pattern`.

        Returns path or none.
        '''
        if not pattern:
            return
        if (2 <= len(pattern) and
            pattern[0] in self.address_characters and
            pattern[0] == pattern[1]):
            prefix = pattern[:2]
            pattern = pattern[2:]
        elif pattern[0] in self.address_characters:
            prefix = pattern[:1]
            pattern = pattern[1:]
        else:
            prefix = ''
        result = []
        if pattern == '<':
            path = self.get_previous_package(cyclic=True)
            if path:
                result.append(path)
        elif pattern == '>':
            path = self.get_next_package(cyclic=True)
            if path:
                result.append(path)
        elif abjad.mathtools.is_integer_equivalent(pattern):
            segment_number = int(pattern)
            path = self.segment_number_to_path(segment_number)
            if path:
                result.append(path)
        elif self.is_dir():
            paths = self.list_paths()
            if self.is_package_path():
                paths.extend(self.contents.list_paths())
                paths.append(self._segments)
                paths.extend(self.builds.list_paths())
                paths.extend(self._segments.list_paths())
                paths.extend(self.distribution.list_paths())
                paths.extend(self.etc.list_paths())
                paths.extend(self.materials.list_paths())
                for path in self.materials.list_paths():
                    paths.extend(path.list_paths())
                paths.extend(self.segments.list_paths())
                for path in self.segments.list_paths():
                    paths.extend(path.list_paths())
                paths.extend(self.stylesheets.list_paths())
                paths.extend(self.test.list_paths())
                paths.extend(self.tools.list_paths())
            if prefix.startswith('@'):
                suffixes = self.configuration.editor_suffixes
                paths = [
                    _ for _ in paths if _.suffix in suffixes or _.is_dir()
                    ]
            elif prefix.startswith('#'):
                paths = [_ for _ in paths if _.suffix == '.py' or _.is_dir()]
            elif prefix.startswith('%'):
                paths = [_ for _ in paths if _.is_dir()]
            elif prefix.startswith('*'):
                paths = [_ for _ in paths if _.suffix == '.pdf' or _.is_dir()]
            elif prefix.startswith('^'):
                paths = [_ for _ in paths if _.suffix == '.py' or _.is_dir()]
            else:
                raise ValueError(repr(prefix))
            strings = [_.get_identifier() for _ in paths]
            if all:
                matches = self.smart_match(strings, pattern, all=True)
                if matches:
                    indices = []
                    for match in set(matches):
                        for i, string in enumerate(strings):
                            if string == match:
                                indices.append(i)
                    for i in sorted(indices):
                        path = paths[i]
                        result.append(path)
            else:
                match = self.smart_match(strings, pattern)
                if match is not None:
                    path = paths[strings.index(match)]
                    result.append(path)
        result_ = []
        for path in result:
            if prefix[0] in ('@', '#', '^') and path.is_dir():
                path /= 'definition.py'
            elif prefix[0] == '*' and path.is_dir():
                path /= 'illustration.pdf'
            if prefix[0] == '%' or path.is_file():
                result_.append(Path(path))
        if all:
            return result_
        elif result_ and len(result_) == 1:
            return result_[0]

    def match_prototype(self, prototype):
        r'''Is true when path matches `prototype`.

        Returns true or false.
        '''
        if prototype is True:
            return True
        if bool(prototype) is False:
            return False
        return self.is_package_path(prototype)

    @staticmethod
    def smart_match(strings, pattern, all=False):
        r'''Matches `pattern` against `strings`.

        ..  container:: example

            ::

                >>> strings = [
                ...     'AcciaccaturaSpecifier.py',
                ...     'AnchorCommand.py',
                ...     'ArpeggiationSpacingSpecifier.py',
                ...     'AttachCommand.py',
                ...     'ChordalSpacingSpecifier.py',
                ...     ]

            ::

                >>> ide.Path.smart_match(strings, 'A') is None
                True

            ::

                >>> ide.Path.smart_match(strings, 'At')
                'AttachCommand.py'

            ::

                >>> ide.Path.smart_match(strings, 'AtC')
                'AttachCommand.py'

            ::

                >>> ide.Path.smart_match(strings, 'ASS')
                'ArpeggiationSpacingSpecifier.py'

            ::

                >>> ide.Path.smart_match(strings, 'AC')
                'AnchorCommand.py'

            ::

                >>> ide.Path.smart_match(strings, '.py')
                'AcciaccaturaSpecifier.py'

            ::

                >>> ide.Path.smart_match(strings, '@AC') is None
                True

        ..  container:: example

            Regression:

            ::

                >>> ide.Path.smart_match(strings, '||') is None
                True

        Returns string or none.
        '''
        if not pattern or pattern[0] in Path.address_characters:
            return
        pattern = abjad.String(pattern)
        matches = []
        for string in strings:
            if string == pattern:
                if all:
                    matches.append(string)
                else:
                    return string
        if 3 <= len(pattern):
            for string in strings:
                if string.startswith(pattern):
                    if all:
                        matches.append(string)
                    else:
                        return string
        if len(pattern) <= 1:
            if not all:
                return
        strings = [abjad.String(_) for _ in strings]
        if not pattern.islower() or any(_.isdigit() for _ in pattern):
            pattern_words = pattern.delimit_words(separate_caps=True)
            if pattern_words:
                for string in strings:
                    if (string.startswith(pattern_words[0]) and
                        string.match_word_starts(pattern_words)):
                        if all:
                            matches.append(string)
                        else:
                            return string
                for string in strings:
                    if string.match_word_starts(pattern_words):
                        if all:
                            matches.append(string)
                        else:
                            return string
        if pattern.islower():
            pattern_characters = list(pattern)
            if pattern_characters:
                for string in strings:
                    if (string.startswith(pattern_characters[0]) and
                        string.match_word_starts(pattern_characters)):
                        if all:
                            matches.append(string)
                        else:
                            return string
                for string in strings:
                    if string.match_word_starts(pattern_characters):
                        if all:
                            matches.append(string)
                        else:
                            return string
        if len(pattern) <= 2:
            if not all:
                return
        for string in strings:
            if pattern.lower() in string.strip_diacritics().lower():
                if all:
                    matches.append(string)
                else:
                    return string
        if all:
            return matches
