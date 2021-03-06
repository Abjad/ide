import ide

abjad_ide = ide.AbjadIDE(test=True)
scores = ide.configuration.test_scores_directory


def test_AbjadIDE_make_illustration_ly_01():
    """
    In segment directory.
    """

    with ide.Test():
        segment = ide.Path(scores, "red_score", "red_score", "segments", "02")
        ly = segment / "illustration.ly"
        ly.remove()
        maker = segment / "__make_segment_ly__.py"
        maker.remove()

        abjad_ide("red gg 02 ilm q")
        transcript = abjad_ide.io.transcript
        assert f"Removing {ly.trim()} ..." not in transcript
        assert f"Writing {maker.trim()} ..." in transcript
        assert f"Interpreting {maker.trim()} ..." in transcript
        assert f"Removing {maker.trim()} ..." in transcript
        assert f"Opening {ly.trim()} ..." not in transcript
        assert ly.is_file()
        assert not maker.exists()

        abjad_ide("red gg 02 ilm q")
        transcript = abjad_ide.io.transcript
        assert f"Removing {ly.trim()} ..." in transcript
        assert f"Writing {maker.trim()} ..." in transcript
        assert f"Interpreting {maker.trim()} ..." in transcript
        assert f"Removing {maker.trim()} ..." in transcript
        assert f"Opening {ly.trim()} ..." not in transcript
        assert ly.is_file()
        assert not maker.exists()
