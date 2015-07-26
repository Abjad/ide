# -*- encoding: utf-8 -*-
import pytest
import os
from abjad import *
import ide
abjad_ide = ide.idetools.AbjadIDE(is_test=True)


def test_PackageWrangler_rename_package_01():
    r'''Renames score package.
    '''
    pytest.skip('make me work again.')

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
        manager = ide.idetools.ScorePackageManager
        manager = manager(path=path_100, session=abjad_ide._session)
        title = 'Example Score 100'
        manager._add_metadatum('title', title)
        input_ = 'ren Example~Score~100 example_score_101 y q'
        abjad_ide._run(input_=input_)
        assert not os.path.exists(path_100)
        assert os.path.exists(path_101)


def test_PackageWrangler_rename_package_02():
    r'''Renames material package.
    '''

    path = os.path.join(
        abjad_ide._configuration.example_score_packages_directory,
        'red_example_score',
        'red_example_score',
        'materials',
        'test_material',
        )
    new_path = os.path.join(
        abjad_ide._configuration.example_score_packages_directory,
        'red_example_score',
        'red_example_score',
        'materials',
        'new_test_material',
        )

    with systemtools.FilesystemState(remove=[path, new_path]):
        input_ = 'red~example~score m new test~material y q'
        abjad_ide._run(input_=input_)
        assert os.path.exists(path)
        input_ = 'red~example~score m ren test~material new~test~material y q'
        abjad_ide._run(input_=input_)
        assert not os.path.exists(path)
        assert os.path.exists(new_path)


def test_PackageWrangler_rename_package_03():
    r'''Renames segment package.
    '''

    path = os.path.join(
        abjad_ide._configuration.example_score_packages_directory,
        'red_example_score',
        'red_example_score',
        'segments',
        'segment_04',
        )
    new_path = os.path.join(
        abjad_ide._configuration.example_score_packages_directory,
        'red_example_score',
        'red_example_score',
        'segments',
        'renamed_segment_04',
        )

    with systemtools.FilesystemState(remove=[path, new_path]):
        input_ = 'red~example~score g new segment~04 y q'
        abjad_ide._run(input_=input_)
        assert os.path.exists(path)
        input_ = 'red~example~score g ren segment~04 renamed_segment_04 y q'
        abjad_ide._run(input_=input_)
        assert not os.path.exists(path)
        assert os.path.exists(new_path)