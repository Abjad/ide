# -*- encoding: utf-8 -*-
from abjad import *
import ide
abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)


def test_Wrangler_display_every_asset_status_01():
    r'''Works with all scores.
    '''

    input_ = 'st* q'
    abjad_ide._run(input_=input_)
    contents = abjad_ide._session._transcript.contents

    assert 'Repository status for' in contents
    assert '... OK' in contents