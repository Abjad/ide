# -*- encoding: utf-8 -*-
from abjad import *
import abjadide
ide = abjadide.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageWrangler_edit_score_stylesheet_01():

    input_ = 'red~example~score k sse q'
    ide._run(input_=input_)

    assert ide._session._attempted_to_open_file