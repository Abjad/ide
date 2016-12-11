# -*- coding: utf-8 -*-
import abjad
import ide
import pytest


def test_MenuSection_default_index_01():

    menu = ide.tools.idetools.Menu()
    commands = []
    commands.append('apple')
    commands.append('banana')
    commands.append('cherry')
    section = menu._make_section(
        menu_entries=commands,
        name='test', 
        title='section',
        )

    assert section.default_index is None


def test_MenuSection_default_index_02():

    menu = ide.tools.idetools.Menu()
    commands = []
    commands.append('apple')
    commands.append('banana')
    commands.append('cherry')
    section = menu._make_section(
        default_index=2,
        menu_entries=commands,
        name='test',
        title='section',
        )

    assert section.default_index == 2
