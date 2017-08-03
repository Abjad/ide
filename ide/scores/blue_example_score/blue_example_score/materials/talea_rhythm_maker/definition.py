import abjad


talea_rhythm_maker = abjad.rhythmmakertools.TaleaRhythmMaker(
    talea=abjad.rhythmmakertools.Talea(
        counts=(2, 2, -3),
        denominator=8,
        ),
    split_divisions_by_counts=(2, 1),
    extra_counts_per_division=(3, 1, 1),
    )
