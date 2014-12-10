# -*- encoding: utf-8 -*-
from abjad import *
import abjadide
ide = abjadide.idetools.AbjadIDE(is_test=True)


def test_BuildFileWrangler_write_views_py_01():

    input_ = 'red~example~score u ww y q'
    ide._run(input_=input_)
    contents = ide._transcript.contents

    assert 'Will write ...' in contents
    assert 'Wrote' in contents