# -*- coding: utf-8 -*-
from abjad import *
from red_example_score.materials.magic_numbers.definition import magic_numbers


def __illustrate__(magic_numbers):
    strings = [str(_) for _ in magic_numbers]
    string = ' '.join(strings)
    markup = Markup(string)
    lilypond_file = lilypondfiletools.LilyPondFile()
    lilypond_file.items.append(markup)
    return lilypond_file