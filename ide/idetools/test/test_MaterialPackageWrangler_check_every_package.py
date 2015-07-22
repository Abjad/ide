# -*- encoding: utf-8 -*-
import os
import shutil
from abjad import *
import ide
abjad_ide = ide.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageWrangler_check_every_package_01():
    r'''Works in score.
    '''

    lines = [
        'Materials directory (5 packages)',
        'Magic numbers: OK',
        'Performer inventory: OK',
        'Pitch range inventory: OK',
        'Tempo inventory: OK',
        'Time signatures: OK',
        ]

    input_ = 'red~example~score m ck* y n q'
    abjad_ide._run(input_=input_)
    contents = abjad_ide._transcript.contents
    for line in lines:
        assert line in contents


def test_MaterialPackageWrangler_check_every_package_02():
    r'''Works at home screen.
    '''

    lines = [
        'Magic numbers (Red Example Score): OK',
        'Performer inventory (Red Example Score): OK',
        'Pitch range inventory (Red Example Score): OK',
        'Tempo inventory (Red Example Score): OK',
        'Time signatures (Red Example Score): OK',
        ]

    input_ = 'mm ck* y n q'
    abjad_ide._run(input_=input_)
    contents = abjad_ide._transcript.contents
    for line in lines:
        assert line in contents

def test_MaterialPackageWrangler_check_every_package_03():
    r'''Supplies missing directory and missing file.
    '''

    material_directory = os.path.join(
        abjad_ide._configuration.example_score_packages_directory,
        'red_example_score',
        'red_example_score',
        'materials',
        'tempo_inventory',
        )
    initializer = os.path.join(material_directory, '__init__.py')
        
    with systemtools.FilesystemState(keep=[initializer]):
        os.remove(initializer)
        input_ = 'red~example~score m ck* y y q'
        abjad_ide._run(input_=input_)
        assert os.path.isfile(initializer)