import abjad
import ide
abjad_ide = ide.AbjadIDE(test=True)


def test_AbjadIDE_git_diff_01():
    """
    In score package directories.
    """

    path = ide.Path('red_score')

    abjad_ide('red diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript

    abjad_ide('red bb diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript

    abjad_ide('red dd diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript

    abjad_ide('red ee diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript

    abjad_ide('red oo diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript

    abjad_ide('red mm diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript

    abjad_ide('red %rpc diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript

    abjad_ide('red gg diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript

    abjad_ide('red %A diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript

    abjad_ide('red yy diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript

    abjad_ide('red tt diff q')
    transcript = abjad_ide.io.transcript
    assert 'Running git diff ...' in transcript


def test_AbjadIDE_git_diff_02():
    """
    In scores directory only.
    """

    abjad_ide('diff q')
    transcript = abjad_ide.io.transcript
    for path in [ide.Path('red_score'), ide.Path('blue_score')]:
        assert f'{path.wrapper} ...' in transcript
        assert 'Running git diff ...' in transcript
