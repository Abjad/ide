import ide
abjad_ide = ide.AbjadIDE(is_test=True)


def test_AbjadIDE_go_to_previous_score_01():
    r'''In materials directory.
    '''

    abjad_ide('red~score mm << << << q')
    transcript = abjad_ide.io.transcript
    assert transcript.titles == [
        'Abjad IDE : scores',
        'Red Score (2017)',
        'Red Score (2017) : materials',
        'Blue Score (2017)',
        'Red Score (2017)',
        'Blue Score (2017)',
        ]


def test_AbjadIDE_go_to_previous_score_02():
    r'''In scores directory.
    '''

    abjad_ide('<< << << q')
    transcript = abjad_ide.io.transcript
    assert transcript.titles == [
        'Abjad IDE : scores',
        'Red Score (2017)',
        'Blue Score (2017)',
        'Red Score (2017)',
        ]
