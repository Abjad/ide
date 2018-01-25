import ide
abjad_ide = ide.AbjadIDE(test=True)


def test_AbjadIDE_make_layout_ly_01():
    r'''In build directory.
    '''
    
    with ide.Test():
        path = ide.Path('red_score', 'builds', 'letter-score', 'layout.ly')
        assert path.is_file()
        path.remove()
        assert not path.exists()

        abjad_ide('red %let llm q')
        lines = abjad_ide.io.transcript.lines
        assert path.is_file()
        for line in [
            'Interpreting red_score/builds/letter-score/layout.py ...',
            'Writing red_score/builds/letter-score/__make_layout_ly__.py ...',
            'Interpreting red_score/builds/letter-score/__make_layout_ly__.py ...',
            'Removing red_score/builds/letter-score/__make_layout_ly__.py ...',
            ]:
            assert line in lines


def test_AbjadIDE_make_layout_ly_02():
    r'''In parts directory.
    '''
    
    with ide.Test():
        parts = ide.Path('green_score', 'builds', 'arch-a-parts')
        assert not parts.exists()
        path = parts('bass-clarinet-layout.ly')

        abjad_ide('gre bb new parts arch-a-parts arch~a ARCH-A y q')
        assert parts.exists()
        assert not path.exists()

        abjad_ide('gre bb arch-a-parts llm bass q')
        lines = abjad_ide.io.transcript.lines
        assert path.is_file()
        for line in [
            'Interpreting green_score/builds/arch-a-parts/bass_clarinet_layout.py ...',
            'Writing green_score/builds/arch-a-parts/__make_layout_ly__.py ...',
            'Interpreting green_score/builds/arch-a-parts/__make_layout_ly__.py ...',
            'Removing green_score/builds/arch-a-parts/__make_layout_ly__.py ...',
            ]:
            assert line in lines


def test_AbjadIDE_make_layout_ly_03():
    r'''In segment directory.
    '''
    
    with ide.Test():
        path = ide.Path('red_score', 'segments', 'A', 'layout.ly')
        assert path.is_file()
        path.remove()
        assert not path.exists()

        abjad_ide('red %A llm q')
        lines = abjad_ide.io.transcript.lines
        assert path.is_file()
        for line in [
            'Interpreting red_score/segments/A/layout.py ...',
            'Writing red_score/segments/A/__make_layout_ly__.py ...',
            'Interpreting red_score/segments/A/__make_layout_ly__.py ...',
            'Removing red_score/segments/A/__make_layout_ly__.py ...',
            ]:
            assert line in lines