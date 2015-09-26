# -*- coding: utf-8 -*-
from abjad import *
import ide
abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)


def test_AbjadIDE_go_to_segment_directory_01():
    r'''%-navigation.
    '''

    input_ = 'red~example~score %A q'
    abjad_ide._start(input_=input_)
    titles = [
        'Abjad IDE - all score directories',
        'Red Example Score (2013)',
        'Red Example Score (2013) - segments directory - A',
        ]

    assert abjad_ide._io_manager._transcript.titles == titles
    assert not abjad_ide._session._attempted_to_open_file


def test_AbjadIDE_go_to_segment_directory_02():

    input_ = 'red~example~score %X q'
    abjad_ide._start(input_=input_)
    contents = abjad_ide._io_manager._transcript.contents

    titles = [
        'Abjad IDE - all score directories',
        'Red Example Score (2013)',
        ]

    assert abjad_ide._io_manager._transcript.titles == titles
    assert "Matches no display string: '%X'." in contents 