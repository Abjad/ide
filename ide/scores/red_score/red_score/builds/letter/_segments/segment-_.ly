\context Score = "Two-Staff Piano Score" <<
    \context GlobalContext = "Global Context" {
        { % measure
            \time 15/8
            s1 * 15/8
        } % measure
        { % measure
            \time 18/8
            s1 * 9/4
        } % measure
    }
    \context PianoStaff = "Piano Staff" <<
        \context Staff = "RH Staff" {
            \context Voice = "RH Voice" {
                \set PianoStaff.instrumentName = \markup { Piano }
                \set PianoStaff.shortInstrumentName = \markup { Pf. }
                \clef "treble"
                g''4.
                bf''4.
                d''4.
                g'4.
                cs'8.
                af'8.
                a'8.
                e''8.
                bf''4
                ~
                bf''16
                c'4
                ~
                c'16
                fs'4
                ~
                fs'16
                bf'4
                ~
                bf'16
                a''4
                ~
                a''16
                bf''4
                ~
                bf''16
            }
        }
        \context Staff = "LH Staff" {
            \context Voice = "LH Voice" {
                \clef "bass"
                fs4
                ~
                fs16
                d,4
                ~
                d,16
                a4
                ~
                a16
                g,4
                ~
                g,16
                cs4
                ~
                cs16
                a4
                ~
                a16
                b,4.
                bf,4.
                c4.
                e,4.
                bf8.
                af,8.
                bf8.
                fs8.
            }
        }
    >>
>>