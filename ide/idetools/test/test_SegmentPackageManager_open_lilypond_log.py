# -*- encoding: utf-8 -*-
from abjad import *
import ide
abjad_ide = ide.idetools.AbjadIDE(is_test=True)


def test_SegmentPackageManager_open_lilypond_log_01():

    input_ = 'red~example~score g A ll q'
    abjad_ide._run(input_=input_)
    
    assert abjad_ide._session._attempted_to_open_file