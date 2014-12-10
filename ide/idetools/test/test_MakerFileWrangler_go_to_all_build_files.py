# -*- encoding: utf-8 -*-
from abjad import *
import ide
abjad_ide = ide.idetools.AbjadIDE(is_test=True)


def test_MakerFileWrangler_go_to_all_build_files_01():
    r'''From makers directory to build depot.
    '''

    input_ = 'red~example~score k uu q'
    abjad_ide._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - makers directory',
        'Abjad IDE - build depot',
        ]
    assert abjad_ide._transcript.titles == titles


def test_MakerFileWrangler_go_to_all_build_files_02():
    r'''From makers depot to build depot.
    '''

    input_ = 'kk uu q'
    abjad_ide._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - makers depot',
        'Abjad IDE - build depot',
        ]
    assert abjad_ide._transcript.titles == titles