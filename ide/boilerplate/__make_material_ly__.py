import abjad
import pathlib
import sys
import traceback


if __name__ == '__main__':

    try:
        from __illustrate__ import lilypond_file
    except ImportError:
        traceback.print_exc()
        sys.exit(1)

    try:
        current_directory = pathlib.Path(__file__).parent
        candidate_path = current_directory / 'illustration.candidate.ly'
        abjad.persist(lilypond_file).as_ly(candidate_path)
    except:
        traceback.print_exc()
        sys.exit(1)

    sys.exit(0)
