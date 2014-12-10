# -*- encoding: utf-8 -*-
from abjad import *
import abjadide
ide = abjadide.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageWrangler_go_to_all_scores_01():

    input_ = 'red~example~score m ss q'
    ide._run(input_=input_)

    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials directory',
        'Abjad IDE - scores',
        ]
    assert ide._transcript.titles == titles


def test_MaterialPackageWrangler_go_to_all_scores_02():

    input_ = 'mm ss q'
    ide._run(input_=input_)

    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - materials depot',
        'Abjad IDE - scores',
        ]
    assert ide._transcript.titles == titles