# -*- encoding: utf-8 -*-
from abjad import *
import ide
abjad_ide = ide.idetools.AbjadIDE(is_test=True)


def test_SegmentPackageWrangler_go_to_next_score_01():

    input_ = 'red~example~score g >> q'
    abjad_ide._run(input_=input_)

    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - segments directory',
        'Blue Example Score (2013)',
        ]
    assert abjad_ide._transcript.titles == titles


def test_SegmentPackageWrangler_go_to_next_score_02():

    input_ = 'gg >> q'
    abjad_ide._run(input_=input_)

    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - segments depot',
        'Blue Example Score (2013)',
        ]
    assert abjad_ide._transcript.titles == titles