# -*- encoding: utf-8 -*-
from abjad import *
import abjadide
ide = abjadide.idetools.AbjadIDE(is_test=True)


def test_SegmentPackageWrangler_display_session_variables_01():
    
    input_ = 'red~example~score g sv q'
    ide._run(input_=input_)
    contents = ide._transcript.contents

    assert 'command_history' in contents
    assert 'controller_stack' in contents


def test_SegmentPackageWrangler_display_session_variables_02():
    
    input_ = 'gg sv q'
    ide._run(input_=input_)
    contents = ide._transcript.contents

    assert 'command_history' in contents
    assert 'controller_stack' in contents