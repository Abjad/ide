# -*- encoding: utf-8 -*-
import os
from abjad import *
import ide
abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)


def test_PackageManager_interpret_illustration_ly_01():
    r'''Works when illustration.ly already exists in material package.
    '''

    ly_path = os.path.join(
        abjad_ide._configuration.example_scores_directory,
        'red_example_score',
        'red_example_score',
        'materials',
        'tempo_inventory',
        'illustration.ly',
        )
    pdf_path = os.path.join(
        abjad_ide._configuration.example_scores_directory,
        'red_example_score',
        'red_example_score',
        'materials',
        'tempo_inventory',
        'illustration.pdf',
        )

    with systemtools.FilesystemState(keep=[ly_path, pdf_path]):
        os.remove(pdf_path)
        assert not os.path.exists(pdf_path)
        input_ = 'red~example~score m tempo~inventory ii y q'
        abjad_ide._run(input_=input_)
        assert os.path.isfile(pdf_path)
        assert systemtools.TestManager._compare_backup(pdf_path)


def test_PackageManager_interpret_illustration_ly_02():
    r'''Works when illustration.ly already exists in segment package.
    '''

    ly_path = os.path.join(
        abjad_ide._configuration.example_scores_directory,
        'red_example_score',
        'red_example_score',
        'segments',
        'segment_01',
        'illustration.ly',
        )
    pdf_path = os.path.join(
        abjad_ide._configuration.example_scores_directory,
        'red_example_score',
        'red_example_score',
        'segments',
        'segment_01',
        'illustration.pdf',
        )

    with systemtools.FilesystemState(keep=[ly_path, pdf_path]):
        os.remove(pdf_path)
        assert not os.path.exists(pdf_path)
        input_ = 'red~example~score g A ii y q'
        abjad_ide._run(input_=input_)
        assert os.path.isfile(pdf_path)
        assert systemtools.TestManager._compare_backup(pdf_path)