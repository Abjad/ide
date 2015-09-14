# -*- coding: utf-8 -*-
import os
from abjad import *
import ide
abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)
configuration = ide.tools.idetools.AbjadIDEConfiguration()


def test_AbjadIDE_new_01():
    r'''Makes new score package.
    '''

    outer_path = os.path.join(
        configuration.composer_scores_directory,
        'example_score',
        )
    inner_path = os.path.join(outer_path, 'example_score')
    outer_directory_entries = [
        'README.md',
        'requirements.txt',
        'setup.cfg',
        'setup.py',
        ]
    inner_directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'build',
        'distribution',
        'etc',
        'makers',
        'materials',
        'segments',
        'stylesheets',
        'test',
        ]

    input_ = 'new Example~Score y q'

    with systemtools.FilesystemState(remove=[outer_path]):
        abjad_ide._run_main_menu(input_=input_)
        contents = abjad_ide._io_manager._transcript.contents
        assert os.path.exists(outer_path)
        session = ide.tools.idetools.Session(is_test=True)
        io_manager = ide.tools.idetools.IOManager(session=session)
        assert abjad_ide._list_directory(inner_path) == inner_directory_entries
        for file_name in outer_directory_entries:
            path = os.path.join(outer_path, file_name)
            assert os.path.exists(path)

    assert 'Enter title]> Example Score' in contents


def test_AbjadIDE_new_02():
    r'''Accepts flexible package name input for score packages.
    '''

    score_package = os.path.join(
        configuration.composer_scores_directory,
        'example_score_1',
        )

    with systemtools.FilesystemState(remove=[score_package]):
        input_ = 'new ExampleScore1 y q'
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(score_package)

    with systemtools.FilesystemState(remove=[score_package]):
        input_ = 'new exampleScore1 y q'
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(score_package)

    with systemtools.FilesystemState(remove=[score_package]):
        input_ = 'new EXAMPLE_SCORE_1 y q'
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(score_package)

    with systemtools.FilesystemState(remove=[score_package]):
        input_ = 'new example_score_1 y q'
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(score_package)


def test_AbjadIDE_new_03():
    r'''Makes new material package inside score.
    '''

    session = ide.tools.idetools.Session(is_test=True)
    path = os.path.join(
        configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'materials',
        'testnotes',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'definition.py',
        ]

    input_ = 'Red~Example~Score m new testnotes y q'

    with systemtools.FilesystemState(remove=[path]):
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(path)
        session = ide.tools.idetools.Session(is_test=True)
        io_manager = ide.tools.idetools.IOManager(session=session)
        assert abjad_ide._list_directory(path) == directory_entries


def test_AbjadIDE_new_04():
    r'''Makes new material package outside score.
    '''

    session = ide.tools.idetools.Session(is_test=True)
    path = os.path.join(
        configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'materials',
        'testnotes',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'definition.py',
        ]

    input_ = 'mm new Red~Example~Score testnotes y q'

    with systemtools.FilesystemState(remove=[path]):
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(path)
        session = ide.tools.idetools.Session(is_test=True)
        io_manager = ide.tools.idetools.IOManager(session=session)
        assert abjad_ide._list_directory(path) == directory_entries


def test_AbjadIDE_new_05():
    r'''Makes new segment package inside score.
    '''

    path = os.path.join(
        configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'segments',
        'segment_04',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'definition.py',
        ]

    input_ = 'red~example~score g new segment~04 y q'

    with systemtools.FilesystemState(remove=[path]):
        abjad_ide._run_main_menu(input_=input_)
        contents = abjad_ide._io_manager._transcript.contents
        assert os.path.exists(path)
        session = ide.tools.idetools.Session(is_test=True)
        io_manager = ide.tools.idetools.IOManager(session=session)
        assert abjad_ide._list_directory(path) == directory_entries


def test_AbjadIDE_new_06():
    r'''Makes new segment package outside score.
    '''

    path = os.path.join(
        configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'segments',
        'segment_04',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'definition.py',
        ]

    input_ = 'gg new Red~Example~Score segment~04 y q'

    with systemtools.FilesystemState(remove=[path]):
        abjad_ide._run_main_menu(input_=input_)
        contents = abjad_ide._io_manager._transcript.contents
        assert os.path.exists(path)
        session = ide.tools.idetools.Session(is_test=True)
        io_manager = ide.tools.idetools.IOManager(session=session)
        assert abjad_ide._list_directory(path) == directory_entries


def test_AbjadIDE_new_07():
    r'''Makes new build file inside score.
    '''

    path = os.path.join(
        configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'build',
        'test-file.txt',
        )

    input_ = 'red~example~score u new test-file.txt q'

    with systemtools.FilesystemState(remove=[path]):
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(path)


def test_AbjadIDE_new_08():
    r'''Makes new build file outside score.
    '''

    path = os.path.join(
        configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'build',
        'test-file.txt',
        )

    input_ = 'uu new red~example~score test-file.txt q'

    with systemtools.FilesystemState(remove=[path]):
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(path)


def test_AbjadIDE_new_09():
    r'''Makes new stylesheet inside score.
    '''

    path = os.path.join(
        configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'stylesheets',
        'new-stylesheet.ily',
        )

    input_ = 'red~example~score y new new-stylesheet.ily q'

    with systemtools.FilesystemState(remove=[path]):
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(path)


def test_AbjadIDE_new_10():
    r'''Makes new stylesheet outside score.
    '''

    path = os.path.join(
        configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'stylesheets',
        'new-stylesheet.ily',
        )

    input_ = 'yy new red~example~score new-stylesheet.ily q'

    with systemtools.FilesystemState(remove=[path]):
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(path)


def test_AbjadIDE_new_11():
    r'''Makes new maker file inside score.
    '''

    path = os.path.join(
        configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'makers',
        'NewMaker.py',
        )

    input_ = 'red~example~score k new NewMaker.py q'

    with systemtools.FilesystemState(remove=[path]):
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(path)


def test_AbjadIDE_new_12():
    r'''Makes new maker file outside score.
    '''

    path = os.path.join(
        configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'makers',
        'NewMaker.py',
        )

    input_ = 'kk new red~example~score NewMaker.py q'

    with systemtools.FilesystemState(remove=[path]):
        abjad_ide._run_main_menu(input_=input_)
        assert os.path.exists(path)