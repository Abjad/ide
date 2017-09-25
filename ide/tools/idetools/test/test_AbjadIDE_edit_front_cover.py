import ide
abjad_ide = ide.AbjadIDE(test=True)


def test_AbjadIDE_edit_front_cover_01():
    
    abjad_ide('red %letter fce q')
    transcript = abjad_ide.io.transcript
    path = ide.Path('red_score', 'builds', 'letter', 'front-cover.tex')
    assert f'Editing {path.trim()} ...' in transcript
