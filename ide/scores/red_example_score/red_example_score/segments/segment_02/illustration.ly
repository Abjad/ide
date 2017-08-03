% 2017-08-21 10:46

\version "2.19.65"
\language "english"

#(ly:set-option 'relative-includes #t)

\include "../../stylesheets/stylesheet.ily"

\header {}

\layout {}

\paper {}

\score {
    \context Score = "Two-Staff Piano Score" <<
        \context GlobalContext = "Global Context" {
            {
                \time 3/4
                s1 * 3/4
            }
            {
                s1 * 3/4
            }
            {
                s1 * 3/4
            }
            {
                s1 * 3/4
            }
            {
                s1 * 3/4
            }
        }
        \context PianoStaff = "Piano Staff" <<
            \context Staff = "RH Staff" {
                \context Voice = "RH Voice" {
                    g''4
                    bf''4
                    d''4
                    g'4
                    cs'8
                    af'8
                    a'8
                    e''8
                    bf''4.
                    c'4.
                    fs'4.
                    bf'4.
                    a''8.
                    bf''8.
                    f''8.
                    e'8.
                }
            }
            \context Staff = "LH Staff" {
                \context Voice = "LH Voice" {
                    fs4.
                    d,4.
                    a4.
                    g,4.
                    cs8.
                    a8.
                    b,8.
                    bf,8.
                    c4
                    e,4
                    bf4
                    af,4
                    bf8
                    fs8
                    f,8
                    bf8
                }
            }
        >>
    >>
}