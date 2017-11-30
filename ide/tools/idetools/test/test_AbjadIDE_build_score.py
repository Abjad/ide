import ide
import os
import pytest
abjad_ide = ide.AbjadIDE(test=True)


@pytest.mark.skipif(
    os.environ.get('TRAVIS') == 'true',
    reason="Travis-CI can not find fonts for XeTeX tests."
    )
def test_AbjadIDE_build_score_01():

    with ide.Test():
        abjad_ide('red %letter bld q')
        transcript = abjad_ide.io.transcript
        assert transcript.lines[-53:] == [
            'Building score ...',
            'Collecting segment lys ...',
            'Removing red_score/builds/_segments/segment-_.ly ...',
            'Writing red_score/builds/_segments/segment-_.ly ...',
            'Removing red_score/builds/_segments/segment-A.ly ...',
            'Writing red_score/builds/_segments/segment-A.ly ...',
            'Removing red_score/builds/_segments/segment-B.ly ...',
            'Writing red_score/builds/_segments/segment-B.ly ...',
            'No SEGMENT:BREAK tags found in red_score/builds/_segments/segment-_.ly ...',
            'No SEGMENT:BREAK tags found in red_score/builds/_segments/segment-A.ly ...',
            'No SEGMENT:BREAK tags found in red_score/builds/_segments/segment-B.ly ...',
            'No SEGMENT:EMPTY_START_BAR tags found in red_score/builds/_segments/segment-_.ly ...',
            'No SEGMENT:EMPTY_START_BAR tags found in red_score/builds/_segments/segment-A.ly ...',
            'No SEGMENT:EMPTY_START_BAR tags found in red_score/builds/_segments/segment-B.ly ...',
            'No SEGMENT:FERMATA_MEASURE tags found in red_score/builds/_segments/segment-_.ly ...',
            'No SEGMENT:FERMATA_MEASURE tags found in red_score/builds/_segments/segment-A.ly ...',
            'No SEGMENT:FERMATA_MEASURE tags found in red_score/builds/_segments/segment-B.ly ...',
            '',
            'Generating music ...',
            'Removing red_score/builds/letter/music.ly ...',
            'Examining segments alphabetically ...',
            'Examining red_score/segments/_ ...',
            'Examining red_score/segments/A ...',
            'Examining red_score/segments/B ...',
            'Writing red_score/builds/letter/music.ly ...',
            '',
            'Interpreting music ...',
            'Interpreting red_score/builds/letter/music.ly ...',
            'Writing red_score/builds/letter/music.pdf ...',
            '',
            'Interpreting front cover ...',
            'Interpreting red_score/builds/letter/front-cover.tex ...',
            'Writing red_score/builds/letter/front-cover.pdf ...',
            '',
            'Interpreting preface ...',
            'Interpreting red_score/builds/letter/preface.tex ...',
            'Writing red_score/builds/letter/preface.pdf ...',
            '',
            'Interpreting back cover ...',
            'Interpreting red_score/builds/letter/back-cover.tex ...',
            'Writing red_score/builds/letter/back-cover.pdf ...',
            '',
            'Generating score ...',
            'Removing red_score/builds/letter/score.tex ...',
            'Writing red_score/builds/letter/score.tex ...',
            '',
            'Interpreting score ...',
            'Interpreting red_score/builds/letter/score.tex ...',
            'Writing red_score/builds/letter/score.pdf ...',
            'Opening red_score/builds/letter/score.pdf ...',
            '',
            '> q',
            '',
            ]
