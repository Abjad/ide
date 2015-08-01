# -*- encoding: utf-8 -*-
from abjad import *
import ide
abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)


def test_PackageManager_display_action_commands_01():
    r'''In material package.
    '''
    
    input_ = 'red~example~score m tempo~inventory ? q'
    abjad_ide._run(input_=input_)
    contents = abjad_ide._session._transcript.contents

    assert 'tempo inventory - action commands' in contents


def test_PackageManager_display_action_commands_02():
    r'''In segment package.
    '''
    
    input_ = 'red~example~score g A ? q'
    abjad_ide._run(input_=input_)
    contents = abjad_ide._session._transcript.contents

    assert 'segments directory - A - action commands' in contents


def test_PackageManager_display_action_commands_03():
    r'''In score package.
    '''
    
    input_ = 'red~example~score ? q'
    abjad_ide._run(input_=input_)
    contents = abjad_ide._session._transcript.contents

    assert 'Red Example Score (2013) - action commands' in contents