import ide

abjad_ide = ide.AbjadIDE(test=True)
scores = ide.configuration.test_scores_directory


def test_AbjadIDE_nake_illustration_pdf_01():
    """
    In segment directory.
    """

    with ide.Test():
        directory = ide.Path(scores, "red_score", "red_score", "segments", "02")
        ly = directory / "illustration.ly"
        ly.remove()
        pdf = directory / "illustration.pdf"
        pdf.remove()
        maker = directory / "__make_segment_pdf__.py"
        maker.remove()

        abjad_ide("red gg 02 ipn q")
        transcript = abjad_ide.io.transcript
        assert "Making segment 02 PDF ..." in transcript
        assert f"Removing {ly.trim()} ..." not in transcript
        assert f"Removing {pdf.trim()} ..." not in transcript
        assert f"Writing {maker.trim()} ..." in transcript
        assert f"Interpreting {maker.trim()} ..." in transcript
        assert f"Found {ly.trim()} ..." in transcript
        assert f"Found {pdf.trim()} ..." in transcript
        assert f"Removing {maker.trim()} ..." in transcript
        assert f"Opening {pdf.trim()} ..." not in transcript
        assert ly.is_file()
        assert pdf.is_file()
        assert not maker.exists()
