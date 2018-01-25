import ide
abjad_ide = ide.AbjadIDE(test=True)


def test_AbjadIDE_interpret_part_tex_01():
    
    with ide.Test():
        parts = ide.Path('green_score', 'builds', 'arch-a-parts')
        part_tex = parts('bass-clarinet-part.tex')
        part_pdf = part_tex.with_suffix('.pdf')
        assert not parts.exists()
        assert not part_tex.exists()
        assert not part_pdf.exists()

        abjad_ide('gre bb new parts arch-a-parts arch~a ARCH-A y q')
        assert parts.exists()
        assert part_tex.is_file()
        assert not part_pdf.exists()
        
        for name in [
            'bass-clarinet-front-cover.pdf',
            'bass-clarinet-preface.pdf',
            'bass-clarinet-music.pdf',
            'bass-clarinet-back-cover.pdf',
            ]:
            abjad_ide._copy_boilerplate(parts, 'blank.pdf', name)

        abjad_ide('gre bb arch pti bass q')
        transcript = abjad_ide.io.transcript
        assert f'Interpreting {part_tex.trim()} ...' in transcript
        assert parts.exists()
        assert part_tex.is_file()
        assert part_pdf.is_file()
