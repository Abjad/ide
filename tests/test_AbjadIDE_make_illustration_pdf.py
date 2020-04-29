import abjad
import ide

abjad_ide = ide.AbjadIDE(test=True)


def test_AbjadIDE_make_illustration_pdf_01():
    """
    In segment directory.
    """

    with ide.Test():
        directory = ide.Path("red_score", "segments", "A")
        ly = directory / "illustration.ly"
        ly.remove()
        pdf = directory / "illustration.pdf"
        pdf.remove()
        maker = directory / "__make_segment_pdf__.py"
        maker.remove()

        abjad_ide("red %A ipm q")
        transcript = abjad_ide.io.transcript
        assert "Making segment A PDF ..." in transcript
        assert f"Removing {ly.trim()} ..." not in transcript
        assert f"Removing {pdf.trim()} ..." not in transcript
        assert f"Writing {maker.trim()} ..." in transcript
        assert f"Interpreting {maker.trim()} ..." in transcript
        assert f"Found {ly.trim()} ..." in transcript
        assert f"Found {pdf.trim()} ..." in transcript
        assert f"Removing {maker.trim()} ..." in transcript
        assert f"Opening {pdf.trim()} ..." in transcript
        assert ly.is_file()
        assert pdf.is_file()
        assert not maker.exists()

        abjad_ide("red %A ipm q")
        transcript = abjad_ide.io.transcript
        assert "Making segment A PDF ..." in transcript
        assert f"Removing {ly.trim()} ..." in transcript
        assert f"Removing {pdf.trim()} ..." in transcript
        assert f"Writing {maker.trim()} ..." in transcript
        assert f"Interpreting {maker.trim()} ..." in transcript
        assert f"Found {ly.trim()} ..." in transcript
        assert f"Found {pdf.trim()} ..." in transcript
        assert f"Removing {maker.trim()} ..." in transcript
        assert f"Opening {pdf.trim()} ..." in transcript
        assert ly.is_file()
        assert pdf.is_file()
        assert not maker.exists()


def test_AbjadIDE_make_illustration_pdf_02():
    """
    In segments directory.
    """

    with ide.Test():
        directory = ide.Path("red_score").segments
        names = ["_", "A", "B"]
        for name in names:
            ly = directory / "illustration.ly"
            ly.remove()
            pdf = directory / "illustration.pdf"
            pdf.remove()
            maker = directory / "__make_segment_pdf__.py"
            maker.remove()

        abjad_ide("red gg ipm q")
        transcript = abjad_ide.io.transcript
        for name in names:
            ly = directory / name / "illustration.ly"
            pdf = directory / name / "illustration.pdf"
            maker = directory / name / "__make_segment_pdf__.py"
            assert f"Making segment {name} PDF ..." in transcript
            assert f"Writing {maker.trim()} ..." in transcript
            assert f"Interpreting {maker.trim()} ..." in transcript
            assert f"Found {ly.trim()} ..." in transcript
            assert f"Found {pdf.trim()} ..." in transcript
            assert f"Removing {maker.trim()} ..." in transcript
            assert f"Opening" not in transcript
            assert ly.is_file()
            assert pdf.is_file()
            assert not maker.exists()

        abjad_ide("red gg **llus q")
        transcript = abjad_ide.io.transcript
        for name in names:
            assert "Matching '**llus' to 3 files ..." in transcript

        abjad_ide("red gg **pdf q")
        transcript = abjad_ide.io.transcript
        for name in names:
            assert "Matching '**pdf' to 3 files ..." in transcript

        abjad_ide("red gg ** q")
        transcript = abjad_ide.io.transcript
        for name in names:
            assert "Matching '**' to 3 files ..." in transcript

        abjad_ide("red gg **asdf q")
        transcript = abjad_ide.io.transcript
        assert "Matching '**asdf' to 0 files ..." in transcript
