# -*- encoding: utf-8 -*-
from abjad import *
import ide
abjad_ide = ide.idetools.AbjadIDE(is_test=True)


def test_SegmentPackageManager_display_available_commands_01():
    
    input_ = 'red~example~score g A ?? q'
    abjad_ide._run(input_=input_)
    contents = abjad_ide._transcript.contents

    assert 'segments directory - A - available commands' in contents