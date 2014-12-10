# -*- encoding: utf-8 -*-
from abjad import *
import ide
abjad_ide = ide.idetools.AbjadIDE(is_test=True)


def test_StylesheetWrangler_doctest_01():
    r'''In library.
    '''

    input_ = 'yy dt q'
    abjad_ide._run(input_=input_)
    contents = abjad_ide._transcript.contents

    strings = [
        'Running doctest ...',
        'No testable assets found.',
        ]
    for string in strings:
        assert string in contents

    
def test_StylesheetWrangler_doctest_02():
    r'''In score package.
    '''

    input_ = 'red~example~score y dt q'
    abjad_ide._run(input_=input_)
    contents = abjad_ide._transcript.contents

    strings = [
        'Running doctest ...',
        'No testable assets found.',
        ]
    for string in strings:
        assert string in contents