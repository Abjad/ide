# -*- encoding: utf-8 -*-
import os
from abjad import *
import ide
abjad_ide = ide.idetools.AbjadIDE(is_test=True)


def test_ScorePackageWrangler_remove_packages_01():
    r'''Removes one score package.
    '''

    path = os.path.join(
        abjad_ide._configuration.user_score_packages_directory,
        'example_score_100',
        )

    with systemtools.FilesystemState(remove=[path]):
        input_ = 'new example~score~100 y q'
        abjad_ide._run(input_=input_)
        assert os.path.exists(path)
        manager = ide.idetools.ScorePackageManager
        manager = manager(path=path, session=abjad_ide._session)
        title = 'Example Score 100'
        manager._add_metadatum('title', title)
        input_ = 'rm Example~Score~100 remove q'
        abjad_ide._run(input_=input_)
        assert not os.path.exists(path)


def test_ScorePackageWrangler_remove_packages_02():
    r'''Removes range of score packages.
    '''

    path_100 = os.path.join(
        abjad_ide._configuration.user_score_packages_directory,
        'example_score_100',
        )
    path_101 = os.path.join(
        abjad_ide._configuration.user_score_packages_directory,
        'example_score_101',
        )

    with systemtools.FilesystemState(remove=[path_100, path_101]):
        input_ = 'new example~score~100 y q'
        abjad_ide._run(input_=input_)
        assert os.path.exists(path_100)
        input_ = 'new example~score~101 y q'
        abjad_ide._run(input_=input_)
        assert os.path.exists(path_101)
        manager = ide.idetools.ScorePackageManager
        manager = manager(path=path_100, session=abjad_ide._session)
        title = 'Example Score 100'
        manager._add_metadatum('title', title)
        manager = ide.idetools.ScorePackageManager
        manager = manager(path=path_101, session=abjad_ide._session)
        title = 'Example Score 101'
        manager._add_metadatum('title', title)
        input_ = 'rm Example~Score~100~-~Example~Score~101 remove~2 q'
        abjad_ide._run(input_=input_)
        assert not os.path.exists(path_100)
        assert not os.path.exists(path_101)