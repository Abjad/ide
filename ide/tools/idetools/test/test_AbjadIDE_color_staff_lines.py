import abjad
import baca
import ide
abjad_ide = ide.AbjadIDE(test=True)


def test_AbjadIDE_color_staff_lines_01():
    r'''In build directory.
    '''

    with ide.Test():

        match = baca.tags.staff_lines_color_match
        build = ide.Path('green_score', 'builds', 'arch-a-score')
        path = build('_segments', 'segment-_.ly')

        abjad_ide('gre bb arch-a-score ggc q')
        assert path.is_file()
        assert path.count(match) == ((0, 0), (4, 4))
        
        abjad_ide('gre bb arch-a-score clsl q')
        lines = abjad_ide.io.transcript.lines
        assert path.count(match) == ((4, 4), (0, 0))
        for line in [
            'Found 4 staff lines color tags in arch-a-score ...',
            ' Activating 4 deactivated staff lines color tags in arch-a-score ...',
            ' No already-active staff lines color tags to skip in arch-a-score ...',
            ]:
            assert line in lines

        abjad_ide('gre bb arch-a-score bwsl q')
        lines = abjad_ide.io.transcript.lines
        assert path.count(match) == ((0, 0), (4, 4))
        for line in [
            'Found 4 staff lines color tags in arch-a-score ...',
            ' Deactivating 4 active staff lines color tags in arch-a-score ...',
            ' No already-deactivated staff lines color tags to skip in arch-a-score ...',
            ]:
            assert line in lines

        abjad_ide('gre bb arch-a-score clsl q')
        lines = abjad_ide.io.transcript.lines
        assert path.count(match) == ((4, 4), (0, 0))
        for line in [
            'Found 4 staff lines color tags in arch-a-score ...',
            ' Activating 4 deactivated staff lines color tags in arch-a-score ...',
            ' No already-active staff lines color tags to skip in arch-a-score ...',
            ]:
            assert line in lines


def test_AbjadIDE_color_staff_lines_02():
    r'''In segment directory.
    '''

    with ide.Test():

        match = baca.tags.staff_lines_color_match
        path = ide.Path('green_score', 'segments', '_', 'illustration.ly')
        assert path.is_file()
        assert path.count(match) == ((4, 4), (0, 0))
        
        abjad_ide('gre %_ clsl q')
        lines = abjad_ide.io.transcript.lines
        assert path.count(match) == ((4, 4), (0, 0))
        for line in [
            'Found 4 staff lines color tags in _ ...',
            ' No deactivated staff lines color tags to activate in _ ...',
            ' Skipping 4 already-active staff lines color tags in _ ...',
            ]:
            assert line in lines
        
        abjad_ide('gre %_ bwsl q')
        assert path.count(match) == ((0, 0), (4, 4))
        lines = abjad_ide.io.transcript.lines
        for line in [
            'Found 4 staff lines color tags in _ ...',
            ' Deactivating 4 active staff lines color tags in _ ...',
            ' No already-deactivated staff lines color tags to skip in _ ...',
            ]:
            assert line in lines

        abjad_ide('gre %_ clsl q')
        lines = abjad_ide.io.transcript.lines
        assert path.count(match) == ((4, 4), (0, 0))
        for line in [
            'Found 4 staff lines color tags in _ ...',
            ' Activating 4 deactivated staff lines color tags in _ ...',
            ' No already-active staff lines color tags to skip in _ ...',
            ]:
            assert line in lines