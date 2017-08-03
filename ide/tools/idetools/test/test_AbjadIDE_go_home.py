import ide
abjad_ide = ide.tools.idetools.AbjadIDE(is_test=True)


def test_AbjadIDE_go_home_01():
    r'''From material directory.
    '''

    input_ = 'red~example~score mm tempi h q'
    abjad_ide._start(input_=input_)

    titles = [
        'Abjad IDE - all score directories',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials directory',
        'Red Example Score (2013) - materials directory - tempi',
        'Abjad IDE - all score directories',
        ]
    assert abjad_ide._io_manager._transcript.titles == titles


def test_AbjadIDE_go_home_02():
    r'''From segment directory.
    '''

    input_ = 'red~example~score gg A h q'
    abjad_ide._start(input_=input_)
    titles = [
        'Abjad IDE - all score directories',
        'Red Example Score (2013)',
        'Red Example Score (2013) - segments directory',
        'Red Example Score (2013) - segments directory - A',
        'Abjad IDE - all score directories',
        ]
    assert abjad_ide._io_manager._transcript.titles == titles


def test_AbjadIDE_go_home_03():
    r'''From score directory.
    '''

    input_ = 'red~example~score h q'
    abjad_ide._start(input_=input_)

    titles = [
        'Abjad IDE - all score directories',
        'Red Example Score (2013)',
        'Abjad IDE - all score directories',
        ]
    assert abjad_ide._io_manager._transcript.titles == titles


def test_AbjadIDE_go_home_04():
    r'''From home to home.
    '''

    input_ = 'h q'
    abjad_ide._start(input_=input_)

    titles = [
        'Abjad IDE - all score directories',
        'Abjad IDE - all score directories',
        ]
    assert abjad_ide._io_manager._transcript.titles == titles
