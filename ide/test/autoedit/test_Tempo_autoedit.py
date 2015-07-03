# -*- encoding: utf-8 -*-
from abjad import *
import ide


def test_Tempo_autoedit_01():
    r'''Creates default tempo.
    '''

    target = Tempo()
    session = ide.idetools.Session(is_test=True)
    autoeditor = ide.idetools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'done'
    autoeditor._session._pending_input = input_
    autoeditor._run()

    assert autoeditor.target is target


def test_Tempo_autoedit_02():
    r'''Edits tempo duration with pair.
    '''

    session = ide.idetools.Session(is_test=True)
    autoeditor = ide.idetools.Autoeditor(
        session=session,
        target=Tempo(),
        )
    input_ = 'reference~duration (1, 8) units 98 done'
    autoeditor._session._pending_input = input_
    autoeditor._run()

    assert autoeditor.target == Tempo(Duration(1, 8), 98)


def test_Tempo_autoedit_03():
    r'''Edits tempo duration with duration object.
    '''

    session = ide.idetools.Session(is_test=True)
    autoeditor = ide.idetools.Autoeditor(
        session=session,
        target=Tempo(),
        )
    input_ = 'reference~duration Duration(1, 8) units 98 done'
    autoeditor._session._pending_input = input_
    autoeditor._run()

    assert autoeditor.target == Tempo(Duration(1, 8), 98)