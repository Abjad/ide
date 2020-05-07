import ide

abjad_ide = ide.AbjadIDE(test=True)


def test_AbjadIDE_generate_layout_py_01():
    """In segment directory.
    """

    with ide.Test():
        target = ide.Path("red_score", "segments", "A", "layout.py")
        assert target.is_file()
        target.remove()

        abjad_ide("red %A lpt q")
        assert not target.exists()

        abjad_ide("red %A lpg q")
        transcript = abjad_ide.io.transcript
        assert f"Writing {target.trim()} ..." in transcript
        assert target.is_file()
