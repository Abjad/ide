# -*- encoding: utf-8 -*-
import string


class Command(object):
    r'''Command decorator.
    '''

    ### CLASS VARIABLES ###

    _allowable_menu_section_names = (
        'back-home-quit',
        'basic',
        'build',
        'comparison',
        'display navigation',
        'git',
        'global files',
        'navigation',
        'package',
        'sibling package',
        'sibling score',
        'star',
        'system',
        'view',
        )

    ### INITIALIZER ###

    def __init__(
        self, 
        command_name, 
        description, 
        menu_section_name,
        is_navigation=False,
        is_hidden=True,
        ):
        assert isinstance(command_name, str), repr(command_name)
        assert Command._is_valid_command_name(command_name), repr(command_name)
        self.command_name = command_name
        self.description = description
        assert menu_section_name in self._allowable_menu_section_names, repr(
            menu_section_name)
        self.menu_section_name = menu_section_name
        assert isinstance(is_hidden, bool), repr(is_hidden)
        self.is_hidden = is_hidden
        assert isinstance(is_navigation, bool), repr(is_navigation)
        self.is_navigation = is_navigation

    ### SPECIAL METHODS ###

    def __call__(self, method):
        r'''Calls command decorator on `method`.

        Returns `method` with command name metadatum attached.
        '''
        method.command_name = self.command_name
        method.description = self.description
        method.menu_section_name = self.menu_section_name
        method.is_hidden = self.is_hidden
        method.is_navigation = self.is_navigation
        return method

    ### PRIVATE METHODS ###

    @staticmethod
    def _is_valid_command_name(expr):
        if not isinstance(expr, str):
            return False
        for character in expr:
            if character.islower():
                continue
            if character in string.punctuation:
                continue
            return False
        return True