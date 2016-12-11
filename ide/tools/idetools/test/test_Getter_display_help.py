# -*- coding: utf-8 -*-
import abjad
import ide
abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)


def test_Getter_display_help_01():
    r'''Question mark displays help.
    '''

    input_ = 'red~example~score mm new ? <return> q'
    abjad_ide._start(input_=input_)
    contents = abjad_ide._io_manager._transcript.contents

    string  = 'Value must be string.'
    assert string in contents


def test_Getter_display_help_02():
    r'''Help string displays help.
    '''

    input_ = 'red~example~score mm new help <return> q'
    abjad_ide._start(input_=input_)
    contents = abjad_ide._io_manager._transcript.contents

    string = 'Value must be string.'
    assert string in contents