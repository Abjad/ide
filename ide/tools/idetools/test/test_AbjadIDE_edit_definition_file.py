# -*- coding: utf-8 -*-
from abjad import *
import ide


def test_AbjadIDE_edit_definition_file_01():
    r'''In material directory.
    '''

    abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)
    input_ = 'red~example~score mm magic~numbers df q'
    abjad_ide._start(input_=input_)

    assert abjad_ide._session._attempted_to_open_file


def test_AbjadIDE_edit_definition_file_02():
    r'''@-addressing to material definition file.
    '''

    abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)
    input_ = 'red~example~score @magic q'
    abjad_ide._start(input_=input_)

    assert abjad_ide._session._attempted_to_open_file

    titles = [
        'Abjad IDE - all score directories',
        'Red Example Score (2013)',
        ]
    assert abjad_ide._io_manager._transcript.titles == titles


def test_AbjadIDE_edit_definition_file_03():
    r'''@-addressing to material definition file.
    '''

    abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)
    input_ = 'red~example~score gg @magic q'
    abjad_ide._start(input_=input_)

    assert abjad_ide._session._attempted_to_open_file

    titles = [
        'Abjad IDE - all score directories',
        'Red Example Score (2013)',
        'Red Example Score (2013) - segments directory',
        ]
    assert abjad_ide._io_manager._transcript.titles == titles


def test_AbjadIDE_edit_definition_file_04():
    r'''In segment directory.
    '''

    abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)
    input_ = 'red~example~score gg A df q'
    abjad_ide._start(input_=input_)

    assert abjad_ide._session._attempted_to_open_file


def test_AbjadIDE_edit_definition_file_05():
    r'''@-addressing to segment definition file.
    '''

    abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)
    input_ = 'red~example~score @A q'
    abjad_ide._start(input_=input_)

    assert abjad_ide._session._attempted_to_open_file

    titles = [
        'Abjad IDE - all score directories',
        'Red Example Score (2013)',
        ]
    assert abjad_ide._io_manager._transcript.titles == titles


def test_AbjadIDE_edit_definition_file_06():
    r'''@-addressing to segment definition file.
    '''

    abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)
    input_ = 'red~example~score mm @A q'
    abjad_ide._start(input_=input_)

    assert abjad_ide._session._attempted_to_open_file

    titles = [
        'Abjad IDE - all score directories',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials directory',
        ]
    assert abjad_ide._io_manager._transcript.titles == titles