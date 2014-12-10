# -*- encoding: utf-8 -*-
from abjad import *
import abjadide
ide = abjadide.idetools.AbjadIDE(is_test=True)


def test_DistributionFileWrangler_go_to_score_distribution_files_01():
    r'''From distribution directory to distribution directory.
    '''

    input_ = 'red~example~score d d q'
    ide._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - distribution directory',
        'Red Example Score (2013) - distribution directory',
        ]
    assert ide._transcript.titles == titles