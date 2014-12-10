# -*- encoding: utf-8 -*-
from abjad import *
from abjad.tools import handlertools
import abjadide


def test_PatternedArticulationsHandler_autoedit_01():
    r'''Edits patterned articulations handler.
    '''

    session = abjadide.idetools.Session(is_test=True)
    target = handlertools.PatternedArticulationsHandler()
    session._autoadvance_depth = 1
    autoeditor = abjadide.idetools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = "[['.', '^'], ['.']] (1, 16) (1, 8) cs'' c''' done"
    autoeditor._session._pending_input = input_
    autoeditor._run()

    handler = handlertools.PatternedArticulationsHandler(
        articulation_lists=[['.', '^'], ['.']],
        minimum_duration=Duration(1, 16),
        maximum_duration=Duration(1, 8),
        minimum_written_pitch=NamedPitch("cs''"),
        maximum_written_pitch=NamedPitch("c'''"),
        )

    assert autoeditor.target == handler