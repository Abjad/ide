import ide
abjad_ide = ide.AbjadIDE(is_test='allow_unknown_input')


def test_Menu_junk_input_01():

    abjad_ide('` # $ & ( ) _ = + q')
    transcript = abjad_ide.io.transcript

    assert "Unknown command '`' ..." in transcript
    assert "Unknown command '#' ..." in transcript
    assert "Unknown command '$' ..." in transcript
    assert "Unknown command '&' ..." in transcript
    assert "Unknown command '(' ..." in transcript
    assert "Unknown command ')' ..." in transcript
    assert "Unknown command '_' ..." in transcript
    assert "Unknown command '=' ..." in transcript
    assert "Unknown command '+' ..." in transcript

    abjad_ide('`` ## $$ && (( )) __ == ++ q')
    transcript = abjad_ide.io.transcript

    assert "Unknown command '``' ..." in transcript
    assert "Unknown command '##' ..." in transcript
    assert "Unknown command '$$' ..." in transcript
    assert "Unknown command '&&' ..." in transcript
    assert "Unknown command '((' ..." in transcript
    assert "Unknown command '))' ..." in transcript
    assert "Unknown command '__' ..." in transcript
    assert "Unknown command '==' ..." in transcript
    assert "Unknown command '++' ..." in transcript


def test_Menu_junk_input_02():

    abjad_ide(r'''[ { ] } \ | : ' " , . / q''')
    transcript = abjad_ide.io.transcript

    assert "Unknown command '[' ..." in transcript
    assert "Unknown command '{' ..." in transcript
    assert "Unknown command ']' ..." in transcript
    assert "Unknown command '}' ..." in transcript
    assert r"Unknown command '\\' ..." in transcript
    assert "Unknown command '|' ..." in transcript
    assert "Unknown command ':' ..." in transcript
    assert '''Unknown command "'" ...''' in transcript
    assert '''Unknown command '"' ...''' in transcript
    assert "Unknown command ',' ..." in transcript
    assert "Unknown command '.' ..." in transcript
    assert "Unknown command '/' ..." in transcript

    abjad_ide(r'''[[ {{ ]] }} \\ || :: '' "" ,, // q''')
    transcript = abjad_ide.io.transcript

    assert "Unknown command '[[' ..." in transcript
    assert "Unknown command '{{' ..." in transcript
    assert "Unknown command ']]' ..." in transcript
    assert "Unknown command '}}' ..." in transcript
    assert r"Unknown command '\\\\' ..." in transcript
    assert "Unknown command '||' ..." in transcript
    assert "Unknown command '::' ..." in transcript
    assert '''Unknown command "''" ...''' in transcript
    assert '''Unknown command '""' ...''' in transcript
    assert "Unknown command ',,' ..." in transcript
    assert "Unknown command '//' ..." in transcript