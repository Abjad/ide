import abjad
import ide
abjad_ide = ide.AbjadIDE(is_test=True)


def test_AbjadIDE_show_help_01():
    r'''In build directory.
    '''

    abjad_ide('red~score %letter ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : builds : letter : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    segment lys - collect (lyc)',
        '',
        '    back cover - generate (bcg)',
        '    front cover - generate (fcg)',
        '    music - generate (mg)',
        '    preface - generate (rg)',
        '    score - generate (sg)',
        '    stylesheet - generate (yg)',
        '',
        '    back cover - edit (bce)',
        '    front cover - edit (fce)',
        '    music - edit (me)',
        '    preface - edit (re)',
        '    score - edit (se)',
        '    stylesheet - edit (ye)',
        '',
        '    back cover - interpret (bci)',
        '    front cover - interpret (fci)',
        '    music - interpret (mi)',
        '    preface - interpret (ri)',
        '    score - interpret (si)',
        '',
        '    back cover - open (bco)',
        '    front cover - open (fco)',
        '    music - open (mo)',
        '    preface - open (ro)',
        '',
        '    score pdf - build (bld)',
        '    score pdf - open (so)',
        '',
        '    path - duplicate (dup)',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next score (>>)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_02():
    r'''In builds directory.
    '''

    abjad_ide('red~score bb ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : builds : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    segment lys - collect (lyc)',
        '',
        '    score pdf - open (so)',
        '',
        '    path - duplicate (dup)',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next score (>>)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_03():
    r'''In contents directory.
    '''

    abjad_ide('red~score ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    score pdf - open (so)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next score (>>)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_04():
    r'''In distribution directory.
    '''

    abjad_ide('red~score dd ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : distribution : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    score pdf - open (so)',
        '',
        '    path - duplicate (dup)',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next score (>>)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_05():
    r'''In library.
    '''

    if not abjad_ide._test_external_directory():
        return

    abjad_ide('lib ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Abjad IDE : library : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    path - duplicate (dup)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_06():
    r'''In material directory.
    '''

    abjad_ide('red~score %magic ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : materials : magic_numbers : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    definition file - check (dfk)',
        '    definition file - edit (df)',
        '',
        '    illustrate file - edit (ill)',
        '    illustrate file - make (illm)',
        '',
        '    ly - edit (ly)',
        '    ly - interpret (lyi)',
        '    ly - make (lym)',
        '',
        '    pdf - make (pdfm)',
        '    pdf - open (pdfo)',
        '',
        '    score pdf - open (so)',
        '',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next package (>)',
        '    go to next score (>>)',
        '    go to previous package (<)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_07():
    r'''In materials directory.
    '''

    abjad_ide('red~score mm ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : materials : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '    every definition file - check (dfk*)',
        '    every ly - interpret (lyi*)',
        '    every pdf - make (pdfm*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    score pdf - open (so)',
        '',
        '    path - duplicate (dup)',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next package (>)',
        '    go to next score (>>)',
        '    go to previous package (<)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_08():
    r'''In scores directory.
    '''

    abjad_ide('? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Abjad IDE : scores : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    path - duplicate (dup)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    every package - git commit (ci*)',
        '    every package - git pull (pull*)',
        '    every package - git push (push*)',
        '    every package - git status (st*)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to next score (>>)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_09():
    r'''In segment directory.
    '''

    abjad_ide('red~score %A ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : segments : A : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    definition file - check (dfk)',
        '    definition file - edit (df)',
        '',
        '    ly - edit (ly)',
        '    ly - interpret (lyi)',
        '    ly - make (lym)',
        '',
        '    pdf - make (pdfm)',
        '    pdf - open (pdfo)',
        '',
        '    midi - make (midim)',
        '',
        '    score pdf - open (so)',
        '',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next package (>)',
        '    go to next score (>>)',
        '    go to previous package (<)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_10():
    r'''In segments directory.
    '''

    abjad_ide('red~score gg ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : segments : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '    every definition file - check (dfk*)',
        '    every ly - interpret (lyi*)',
        '    every pdf - make (pdfm*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    score pdf - open (so)',
        '',
        '    path - duplicate (dup)',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next package (>)',
        '    go to next score (>>)',
        '    go to previous package (<)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_11():
    r'''In stylesheets directory.
    '''

    abjad_ide('red~score yy ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : stylesheets : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    score pdf - open (so)',
        '',
        '    path - duplicate (dup)',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next score (>>)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_12():
    r'''In test directory.
    '''

    abjad_ide('red~score tt ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : test : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    score pdf - open (so)',
        '',
        '    path - duplicate (dup)',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next score (>>)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_13():
    r'''In tools directory.
    '''

    abjad_ide('red~score oo ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : tools : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    score pdf - open (so)',
        '',
        '    path - duplicate (dup)',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next score (>>)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]


def test_AbjadIDE_show_help_14():
    r'''In wrapper directory.
    '''

    abjad_ide('red ww ? q')
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        'Red Score (2017) : wrapper : help',
        '',
        '    every - file edit (@@)',
        '    every - pdf open (**)',
        '    every - string edit (ee*)',
        '',
        '    call shell (!)',
        '    force single column (!!)',
        '    go to directory (%)',
        '    replace (rp)',
        '    search (sr)',
        '    show help (?)',
        '',
        '    aliases - edit (als)',
        '    latex log - edit (lxg)',
        '    lilypond log - edit (lpg)',
        '',
        '    tests - all (tests)',
        '    tests - doctest (^)',
        '    tests - pytest (+)',
        '',
        '    clipboard - copy (cp)',
        '    clipboard - empty (ce)',
        '    clipboard - paste (cv)',
        '    clipboard - show (cs)',
        '',
        '    score pdf - open (so)',
        '',
        '    path - duplicate (dup)',
        '    path - get (get)',
        '    path - new (new)',
        '    path - remove (rm)',
        '    path - rename (ren)',
        '',
        '    git - commit (ci)',
        '    git - diff (diff)',
        '    git - pull (pull)',
        '    git - push (push)',
        '    git - status (st)',
        '',
        '    go to library (lib)',
        '    go to scores directory (ss)',
        '',
        '    go to builds directory (bb)',
        '    go to builds segments directory (nn)',
        '    go to contents directory (cc)',
        '    go to distribution directory (dd)',
        '    go to etc directory (ee)',
        '    go to materials directory (mm)',
        '    go to segments directory (gg)',
        '    go to stylesheets directory (yy)',
        '    go to test directory (tt)',
        '    go to tools directory (oo)',
        '    go to wrapper directory (ww)',
        '',                                    
        '    go to next score (>>)',
        '    go to previous score (<<)',
        '',
        '    back (-)',
        '    quit (q)',
        '    up (..)',
        '',
        ]
