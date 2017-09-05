import ide
abjad_ide = ide.AbjadIDE(is_test=True)


def test_AbjadIDE_go_to_next_package_01():
    r'''In materials directory.
    '''

    abjad_ide('red~score mm > > > q')
    transcript = abjad_ide.io_manager.transcript
    assert transcript.titles == [
        'Abjad IDE : scores',
        'Red Score (2017)',
        'Red Score (2017) : materials',
        'Red Score (2017) : materials : magic_numbers',
        'Red Score (2017) : materials : performers',
        'Red Score (2017) : materials : ranges',
        ]


def test_AbjadIDE_go_to_next_package_02():
    r'''In material directory.
    '''

    abjad_ide('red~score mm performers > > q')
    transcript = abjad_ide.io_manager.transcript
    assert transcript.titles == [
        'Abjad IDE : scores',
        'Red Score (2017)',
        'Red Score (2017) : materials',
        'Red Score (2017) : materials : performers',
        'Red Score (2017) : materials : ranges',
        'Red Score (2017) : materials : tempi',
        ]


def test_AbjadIDE_go_to_next_package_03():
    r'''In segments directory.
    '''

    abjad_ide('red~score gg > > > q')
    transcript = abjad_ide.io_manager.transcript
    assert transcript.titles == [
        'Abjad IDE : scores',
        'Red Score (2017)',
        'Red Score (2017) : segments',
        'Red Score (2017) : segments : A',
        'Red Score (2017) : segments : B',
        'Red Score (2017) : segments : C',
        ]


def test_AbjadIDE_go_to_next_package_04():
    r'''In segment directory.
    '''

    abjad_ide('red~score gg A > > q')
    transcript = abjad_ide.io_manager.transcript
    assert transcript.titles == [
        'Abjad IDE : scores',
        'Red Score (2017)',
        'Red Score (2017) : segments',
        'Red Score (2017) : segments : A',
        'Red Score (2017) : segments : B',
        'Red Score (2017) : segments : C',
        ]
