import ide
abjad_ide = ide.AbjadIDE(test=True)


def test_AbjadIDE_git_commit_all_01():

    abjad_ide('ci* Updated. q')
    transcript = abjad_ide.io.transcript
    assert 'Commit message> Updated.' in transcript
    for path in [ide.Path('red_score'), ide.Path('blue_score')]:
        assert f'Git commit {path.wrapper()} ...' in transcript