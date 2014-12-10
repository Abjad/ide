# -*- encoding: utf-8 -*-
from abjad import *
import abjadide
session = abjadide.idetools.Session(is_test=True)


def test_Selector_make_clef_name_selector_01():

    selector = abjadide.idetools.Selector(session=session)
    selector = selector.make_clef_name_selector()
    selector._session._is_test = True
    selector._session._pending_input = 'tre'
    assert selector._run() == 'treble'