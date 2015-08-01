# -*- encoding: utf-8 -*-
from abjad import *
import os
import pytest
import ide
abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)


def test_Wrangler_interpret_front_cover_01():
    r'''Makes front-cover.pdf when front-cover.pdf doesn't yet exist.
    '''

    tex_path = os.path.join(
        abjad_ide._configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'build',
        'front-cover.tex',
        )
    pdf_path = os.path.join(
        abjad_ide._configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'build',
        'front-cover.pdf',
        )

    with systemtools.FilesystemState(keep=[tex_path, pdf_path]):
        os.remove(pdf_path)
        assert not os.path.exists(pdf_path)
        input_ = 'red~example~score u fci q'
        abjad_ide._run(input_=input_)
        assert os.path.isfile(pdf_path)
        assert systemtools.TestManager._compare_backup(pdf_path)


@pytest.mark.skipif(
    os.environ.get('TRAVIS') == 'true',
    reason='Cannot build on Travis-CI',
    )
def test_Wrangler_interpret_front_cover_02():
    r'''Preserves front-cover.pdf when front-cover.candidate.pdf 
    compares equal to front-cover.pdf.
    '''

    tex_path = os.path.join(
        abjad_ide._configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'build',
        'front-cover.tex',
        )
    pdf_path = os.path.join(
        abjad_ide._configuration.abjad_ide_example_scores_directory,
        'red_example_score',
        'red_example_score',
        'build',
        'front-cover.pdf',
        )

    with systemtools.FilesystemState(keep=[tex_path, pdf_path]):
        input_ = 'red~example~score u fci q'
        abjad_ide._run(input_=input_)

    contents = abjad_ide._session._transcript.contents
    assert 'The files ...' in contents
    assert '... compare the same.' in contents
    assert 'Preserved' in contents