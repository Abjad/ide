import ide

abjad_ide = ide.AbjadIDE(test=True)


def test_AbjadIDE_show_help_01():
    """
    In _assets directory.
    """

    abjad_ide("red bb _assets ? q")
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Red Score (2017) : builds : _assets (empty) : help",
        "",
        "    all - edit (@@)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next score (>>)",
        "    hop - previous score (<<)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    path - duplicate (dup)",
        "    path - get (get)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    score.pdf - open (spo)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_02():
    """
    In _segments directory.
    """

    abjad_ide("red bb letter _segments ? q")
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Red Score (2017) : builds : letter-score : _segments (empty) : help",
        "",
        "    all - edit (@@)",
        "",
        "    back-cover.pdf - open (bcpo)",
        "    back-cover.tex - edit (bcte)",
        "    back-cover.tex - generate (bctg)",
        "    back-cover.tex - interpret (bcti)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    front-cover.pdf - open (fcpo)",
        "    front-cover.tex - edit (fcte)",
        "    front-cover.tex - generate (fctg)",
        "    front-cover.tex - interpret (fcti)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next score (>>)",
        "    hop - previous score (<<)",
        "",
        "    .log - edit (le)",
        "",
        "    layout.ly - edit (lle)",
        "    layout.ly - make (llm)",
        "    layout.py - edit (lpe)",
        "    layout.py - generate (lpg)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    music.ly - edit (mle)",
        "    music.ly - generate (mlg)",
        "    music.ly - interpret (mli)",
        "    music.ly - xinterpret (mlx)",
        "    music.pdf - open (mpo)",
        "",
        "    annotation spanners - hide (ash)",
        "    annotation spanners - show (ass)",
        "    clock time - hide (cth)",
        "    clock time - show (cts)",
        "    figure names - hide (fnh)",
        "    figure names - show (fns)",
        "    invisible music - hide (imh)",
        "    invisible music - show (ims)",
        "    local measure numbers - hide (lmnh)",
        "    local measure numbers - show (lmns)",
        "    measure numbers - hide (mnh)",
        "    measure numbers - show (mns)",
        "    mock music - hide (mmh)",
        "    mock music - show (mms)",
        "    music annotations - hide (mah)",
        "    music annotations - show (mas)",
        "    not yet pitched - hide (nyph)",
        "    not yet pitched - show (nyps)",
        "    rhythm annotation spanners - hide (rash)",
        "    rhythm annotation spanners - show (rass)",
        "    spacing - hide (sph)",
        "    spacing - show (sps)",
        "    stage numbers - hide (snh)",
        "    stage numbers - show (sns)",
        "    tag - hide (th)",
        "    tag - show (ts)",
        "",
        "    path - duplicate (dup)",
        "    path - get (get)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    clefs - color (ccl)",
        "    clefs - uncolor (cuc)",
        "    dynamics - color (dcl)",
        "    dynamics - uncolor (duc)",
        "    instruments - color (icl)",
        "    instruments - uncolor (iuc)",
        "    margin markup - color (mmcl)",
        "    margin markup - uncolor (mmuc)",
        "    metronome marks - color (tmcl)",
        "    metronome marks - uncolor (tmuc)",
        "    persistent indicators - color (picl)",
        "    persistent indicators - uncolor (piuc)",
        "    staff lines - color (slcl)",
        "    staff lines - uncolor (sluc)",
        "    time signatures - color (tscl)",
        "    time signatures - uncolor (tsuc)",
        "",
        "    preface.pdf - open (pfpo)",
        "    preface.tex - edit (pfte)",
        "    preface.tex - generate (pftg)",
        "    preface.tex - interpret (pfti)",
        "",
        "    score.pdf - build (spb)",
        "    score.pdf - open (spo)",
        "    score.tex - edit (ste)",
        "    score.tex - generate (stg)",
        "    score.tex - interpret (sti)",
        "",
        "    segments - collect (ggc)",
        "    segments - handle build tags (btags)",
        "    segments - handle part tags (ptags)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    stylesheet.ily - edit (ssie)",
        "    stylesheet.ily - generate (ssig)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_03():
    """
    In build directory.
    """

    abjad_ide("red bb letter ? q")
    menu = abjad_ide.io.transcript.menus[-1]

    assert menu == [
        "Red Score (2017) : builds : letter-score : help",
        "",
        "    all - edit (@@)",
        "",
        "    back-cover.pdf - open (bcpo)",
        "    back-cover.tex - edit (bcte)",
        "    back-cover.tex - generate (bctg)",
        "    back-cover.tex - interpret (bcti)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    front-cover.pdf - open (fcpo)",
        "    front-cover.tex - edit (fcte)",
        "    front-cover.tex - generate (fctg)",
        "    front-cover.tex - interpret (fcti)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next score (>>)",
        "    hop - previous score (<<)",
        "",
        "    .log - edit (le)",
        "",
        "    layout.ly - edit (lle)",
        "    layout.ly - make (llm)",
        "    layout.py - edit (lpe)",
        "    layout.py - generate (lpg)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    music.ly - edit (mle)",
        "    music.ly - generate (mlg)",
        "    music.ly - interpret (mli)",
        "    music.ly - xinterpret (mlx)",
        "    music.pdf - open (mpo)",
        "",
        "    annotation spanners - hide (ash)",
        "    annotation spanners - show (ass)",
        "    clock time - hide (cth)",
        "    clock time - show (cts)",
        "    figure names - hide (fnh)",
        "    figure names - show (fns)",
        "    invisible music - hide (imh)",
        "    invisible music - show (ims)",
        "    local measure numbers - hide (lmnh)",
        "    local measure numbers - show (lmns)",
        "    measure numbers - hide (mnh)",
        "    measure numbers - show (mns)",
        "    mock music - hide (mmh)",
        "    mock music - show (mms)",
        "    music annotations - hide (mah)",
        "    music annotations - show (mas)",
        "    not yet pitched - hide (nyph)",
        "    not yet pitched - show (nyps)",
        "    rhythm annotation spanners - hide (rash)",
        "    rhythm annotation spanners - show (rass)",
        "    spacing - hide (sph)",
        "    spacing - show (sps)",
        "    stage numbers - hide (snh)",
        "    stage numbers - show (sns)",
        "    tag - hide (th)",
        "    tag - show (ts)",
        "",
        "    path - duplicate (dup)",
        "    path - get (get)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    clefs - color (ccl)",
        "    clefs - uncolor (cuc)",
        "    dynamics - color (dcl)",
        "    dynamics - uncolor (duc)",
        "    instruments - color (icl)",
        "    instruments - uncolor (iuc)",
        "    margin markup - color (mmcl)",
        "    margin markup - uncolor (mmuc)",
        "    metronome marks - color (tmcl)",
        "    metronome marks - uncolor (tmuc)",
        "    persistent indicators - color (picl)",
        "    persistent indicators - uncolor (piuc)",
        "    staff lines - color (slcl)",
        "    staff lines - uncolor (sluc)",
        "    time signatures - color (tscl)",
        "    time signatures - uncolor (tsuc)",
        "",
        "    preface.pdf - open (pfpo)",
        "    preface.tex - edit (pfte)",
        "    preface.tex - generate (pftg)",
        "    preface.tex - interpret (pfti)",
        "",
        "    score.pdf - build (spb)",
        "    score.pdf - open (spo)",
        "    score.tex - edit (ste)",
        "    score.tex - generate (stg)",
        "    score.tex - interpret (sti)",
        "",
        "    segments - collect (ggc)",
        "    segments - handle build tags (btags)",
        "    segments - handle part tags (ptags)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    stylesheet.ily - edit (ssie)",
        "    stylesheet.ily - generate (ssig)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_04():
    """
    In builds directory.
    """

    abjad_ide("red bb ? q")
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Red Score (2017) : builds : help",
        "",
        "    all - edit (@@)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next score (>>)",
        "    hop - previous score (<<)",
        "",
        "    .log - edit (le)",
        "",
        "    layout.ly - edit (lle)",
        "    layout.ly - make (llm)",
        "    layout.py - edit (lpe)",
        "    layout.py - generate (lpg)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    annotation spanners - hide (ash)",
        "    annotation spanners - show (ass)",
        "    clock time - hide (cth)",
        "    clock time - show (cts)",
        "    figure names - hide (fnh)",
        "    figure names - show (fns)",
        "    invisible music - hide (imh)",
        "    invisible music - show (ims)",
        "    local measure numbers - hide (lmnh)",
        "    local measure numbers - show (lmns)",
        "    measure numbers - hide (mnh)",
        "    measure numbers - show (mns)",
        "    mock music - hide (mmh)",
        "    mock music - show (mms)",
        "    music annotations - hide (mah)",
        "    music annotations - show (mas)",
        "    not yet pitched - hide (nyph)",
        "    not yet pitched - show (nyps)",
        "    rhythm annotation spanners - hide (rash)",
        "    rhythm annotation spanners - show (rass)",
        "    spacing - hide (sph)",
        "    spacing - show (sps)",
        "    stage numbers - hide (snh)",
        "    stage numbers - show (sns)",
        "    tag - hide (th)",
        "    tag - show (ts)",
        "",
        "    path - duplicate (dup)",
        "    path - get (get)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    clefs - color (ccl)",
        "    clefs - uncolor (cuc)",
        "    dynamics - color (dcl)",
        "    dynamics - uncolor (duc)",
        "    instruments - color (icl)",
        "    instruments - uncolor (iuc)",
        "    margin markup - color (mmcl)",
        "    margin markup - uncolor (mmuc)",
        "    metronome marks - color (tmcl)",
        "    metronome marks - uncolor (tmuc)",
        "    persistent indicators - color (picl)",
        "    persistent indicators - uncolor (piuc)",
        "    staff lines - color (slcl)",
        "    staff lines - uncolor (sluc)",
        "    time signatures - color (tscl)",
        "    time signatures - uncolor (tsuc)",
        "",
        "    score.pdf - open (spo)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_05():
    """
    In contents directory.
    """

    abjad_ide("red ? q")
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Red Score (2017) : help",
        "",
        "    all - edit (@@)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next score (>>)",
        "    hop - previous score (<<)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    score.pdf - open (spo)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_06():
    """
    In distribution directory.
    """

    abjad_ide("red dd ? q")
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Red Score (2017) : distribution : help",
        "",
        "    all - edit (@@)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next score (>>)",
        "    hop - previous score (<<)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    path - duplicate (dup)",
        "    path - get (get)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    score.pdf - open (spo)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_07():
    """
    In parts directory.
    """

    with ide.Test():

        abjad_ide("gre bb new parts arch-a-parts arch~a ARCH-A y q")
        abjad_ide("gre bb arch-a-parts ? q")

    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Green Score (2018) : builds : arch-a-parts : help",
        "",
        "    all - edit (@@)",
        "",
        "    back-cover.pdf - open (bcpo)",
        "    back-cover.tex - edit (bcte)",
        "    back-cover.tex - generate (bctg)",
        "    back-cover.tex - interpret (bcti)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    front-cover.pdf - open (fcpo)",
        "    front-cover.tex - edit (fcte)",
        "    front-cover.tex - generate (fctg)",
        "    front-cover.tex - interpret (fcti)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next score (>>)",
        "    hop - previous score (<<)",
        "",
        "    .log - edit (le)",
        "",
        "    layout.ly - edit (lle)",
        "    layout.ly - make (llm)",
        "    layout.py - edit (lpe)",
        "    layout.py - generate (lpg)",
        "    layout.py - propagate (lpp)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    music.ly - edit (mle)",
        "    music.ly - generate (mlg)",
        "    music.ly - interpret (mli)",
        "    music.ly - xinterpret (mlx)",
        "    music.pdf - open (mpo)",
        "",
        "    annotation spanners - hide (ash)",
        "    annotation spanners - show (ass)",
        "    clock time - hide (cth)",
        "    clock time - show (cts)",
        "    figure names - hide (fnh)",
        "    figure names - show (fns)",
        "    invisible music - hide (imh)",
        "    invisible music - show (ims)",
        "    local measure numbers - hide (lmnh)",
        "    local measure numbers - show (lmns)",
        "    measure numbers - hide (mnh)",
        "    measure numbers - show (mns)",
        "    mock music - hide (mmh)",
        "    mock music - show (mms)",
        "    music annotations - hide (mah)",
        "    music annotations - show (mas)",
        "    not yet pitched - hide (nyph)",
        "    not yet pitched - show (nyps)",
        "    rhythm annotation spanners - hide (rash)",
        "    rhythm annotation spanners - show (rass)",
        "    spacing - hide (sph)",
        "    spacing - show (sps)",
        "    stage numbers - hide (snh)",
        "    stage numbers - show (sns)",
        "    tag - hide (th)",
        "    tag - show (ts)",
        "",
        "    part.pdf - build (ppb)",
        "    part.pdf - open (ppo)",
        "    part.tex - edit (pte)",
        "    part.tex - generate (ptg)",
        "    part.tex - interpret (pti)",
        "",
        "    path - duplicate (dup)",
        "    path - get (get)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    clefs - color (ccl)",
        "    clefs - uncolor (cuc)",
        "    dynamics - color (dcl)",
        "    dynamics - uncolor (duc)",
        "    instruments - color (icl)",
        "    instruments - uncolor (iuc)",
        "    margin markup - color (mmcl)",
        "    margin markup - uncolor (mmuc)",
        "    metronome marks - color (tmcl)",
        "    metronome marks - uncolor (tmuc)",
        "    persistent indicators - color (picl)",
        "    persistent indicators - uncolor (piuc)",
        "    staff lines - color (slcl)",
        "    staff lines - uncolor (sluc)",
        "    time signatures - color (tscl)",
        "    time signatures - uncolor (tsuc)",
        "",
        "    preface.pdf - open (pfpo)",
        "    preface.tex - edit (pfte)",
        "    preface.tex - generate (pftg)",
        "    preface.tex - interpret (pfti)",
        "",
        "    score.pdf - open (spo)",
        "",
        "    segments - collect (ggc)",
        "    segments - handle build tags (btags)",
        "    segments - handle part tags (ptags)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    stylesheet.ily - edit (ssie)",
        "    stylesheet.ily - generate (ssig)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_08():
    """
    In scores directory.
    """

    abjad_ide("? q")
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Abjad IDE : scores : help",
        "",
        "    all - edit (@@)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next score (>>)",
        "    hop - previous score (<<)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    path - duplicate (dup)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    score.pdf - open (spo)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_09():
    """
    In segment directory.
    """

    abjad_ide("red A ? q")
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Red Score (2017) : segments : A : help",
        "",
        "    all - edit (@@)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    definition.py - check (dpc)",
        "    definition.py - edit (dpe)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next package (>)",
        "    hop - next score (>>)",
        "    hop - previous package (<)",
        "    hop - previous score (<<)",
        "",
        "    .log - edit (le)",
        "    .optimization - checkout (oc)",
        "    .optimization - edit (oe)",
        "    illustration.ily - edit (iie)",
        "    illustration.ly - edit (ile)",
        "    illustration.ly - interpret (ili)",
        "    illustration.ly - make (ilm)",
        "    illustration.pdf - make (ipm)",
        "    illustration.pdf - nake (ipn)",
        "    illustration.pdf - open (ipo)",
        "",
        "    layout.ly - edit (lle)",
        "    layout.ly - make (llm)",
        "    layout.py - edit (lpe)",
        "    layout.py - generate (lpg)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    annotation spanners - hide (ash)",
        "    annotation spanners - show (ass)",
        "    clock time - hide (cth)",
        "    clock time - show (cts)",
        "    figure names - hide (fnh)",
        "    figure names - show (fns)",
        "    invisible music - hide (imh)",
        "    invisible music - show (ims)",
        "    local measure numbers - hide (lmnh)",
        "    local measure numbers - show (lmns)",
        "    measure numbers - hide (mnh)",
        "    measure numbers - show (mns)",
        "    mock music - hide (mmh)",
        "    mock music - show (mms)",
        "    music annotations - hide (mah)",
        "    music annotations - show (mas)",
        "    not yet pitched - hide (nyph)",
        "    not yet pitched - show (nyps)",
        "    rhythm annotation spanners - hide (rash)",
        "    rhythm annotation spanners - show (rass)",
        "    spacing - hide (sph)",
        "    spacing - show (sps)",
        "    stage numbers - hide (snh)",
        "    stage numbers - show (sns)",
        "    tag - hide (th)",
        "    tag - show (ts)",
        "",
        "    path - get (get)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    clefs - color (ccl)",
        "    clefs - uncolor (cuc)",
        "    dynamics - color (dcl)",
        "    dynamics - uncolor (duc)",
        "    instruments - color (icl)",
        "    instruments - uncolor (iuc)",
        "    margin markup - color (mmcl)",
        "    margin markup - uncolor (mmuc)",
        "    metronome marks - color (tmcl)",
        "    metronome marks - uncolor (tmuc)",
        "    persistent indicators - color (picl)",
        "    persistent indicators - uncolor (piuc)",
        "    staff lines - color (slcl)",
        "    staff lines - uncolor (sluc)",
        "    time signatures - color (tscl)",
        "    time signatures - uncolor (tsuc)",
        "",
        "    score.pdf - open (spo)",
        "",
        "    clicktrack - make (ctm)",
        "    segment.midi - make (midm)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_10():
    """
    In segments directory.
    """

    abjad_ide("red gg ? q")
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Red Score (2017) : segments : help",
        "",
        "    all - edit (@@)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    definition.py - check (dpc)",
        "    definition.py - edit (dpe)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next package (>)",
        "    hop - next score (>>)",
        "    hop - previous package (<)",
        "    hop - previous score (<<)",
        "",
        "    .log - edit (le)",
        "    .optimization - checkout (oc)",
        "    .optimization - edit (oe)",
        "    illustration.ily - edit (iie)",
        "    illustration.ly - edit (ile)",
        "    illustration.ly - interpret (ili)",
        "    illustration.ly - make (ilm)",
        "    illustration.pdf - make (ipm)",
        "    illustration.pdf - nake (ipn)",
        "    illustration.pdf - open (ipo)",
        "",
        "    layout.ly - edit (lle)",
        "    layout.ly - make (llm)",
        "    layout.py - edit (lpe)",
        "    layout.py - generate (lpg)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    annotation spanners - hide (ash)",
        "    annotation spanners - show (ass)",
        "    clock time - hide (cth)",
        "    clock time - show (cts)",
        "    figure names - hide (fnh)",
        "    figure names - show (fns)",
        "    invisible music - hide (imh)",
        "    invisible music - show (ims)",
        "    local measure numbers - hide (lmnh)",
        "    local measure numbers - show (lmns)",
        "    measure numbers - hide (mnh)",
        "    measure numbers - show (mns)",
        "    mock music - hide (mmh)",
        "    mock music - show (mms)",
        "    music annotations - hide (mah)",
        "    music annotations - show (mas)",
        "    not yet pitched - hide (nyph)",
        "    not yet pitched - show (nyps)",
        "    rhythm annotation spanners - hide (rash)",
        "    rhythm annotation spanners - show (rass)",
        "    spacing - hide (sph)",
        "    spacing - show (sps)",
        "    stage numbers - hide (snh)",
        "    stage numbers - show (sns)",
        "    tag - hide (th)",
        "    tag - show (ts)",
        "",
        "    path - duplicate (dup)",
        "    path - get (get)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    clefs - color (ccl)",
        "    clefs - uncolor (cuc)",
        "    dynamics - color (dcl)",
        "    dynamics - uncolor (duc)",
        "    instruments - color (icl)",
        "    instruments - uncolor (iuc)",
        "    margin markup - color (mmcl)",
        "    margin markup - uncolor (mmuc)",
        "    metronome marks - color (tmcl)",
        "    metronome marks - uncolor (tmuc)",
        "    persistent indicators - color (picl)",
        "    persistent indicators - uncolor (piuc)",
        "    staff lines - color (slcl)",
        "    staff lines - uncolor (sluc)",
        "    time signatures - color (tscl)",
        "    time signatures - uncolor (tsuc)",
        "",
        "    score.pdf - open (spo)",
        "",
        "    clicktrack - make (ctm)",
        "    segment.midi - make (midm)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_11():
    """
    In stylesheets directory.
    """

    abjad_ide("red yy ? q")
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Red Score (2017) : stylesheets : help",
        "",
        "    all - edit (@@)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next score (>>)",
        "    hop - previous score (<<)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    path - duplicate (dup)",
        "    path - get (get)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    score.pdf - open (spo)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]


def test_AbjadIDE_show_help_12():
    """
    In wrapper directory.
    """

    abjad_ide("red ww ? q")
    menu = abjad_ide.io.transcript.menus[-1]
    assert menu == [
        "Red Score (2017) : wrapper : help",
        "",
        "    all - edit (@@)",
        "",
        "    clipboard - copy (cbc)",
        "    clipboard - cut (cbx)",
        "    clipboard - empty (cbe)",
        "    clipboard - paste (cbv)",
        "    clipboard - show (cbs)",
        "",
        "    directory - builds (bb)",
        "    directory - contents (cc)",
        "    directory - distribution (dd)",
        "    directory - etc (ee)",
        "    directory - segments (gg)",
        "    directory - stylesheets (yy)",
        "    directory - wrapper (ww)",
        "",
        "    git - commit (ci)",
        "    git - diff (diff)",
        "    git - pull (pull)",
        "    git - push (push)",
        "    git - status (st)",
        "",
        "    go - back (-)",
        "    go - quit (q)",
        "    go - scores (ss)",
        "    go - up (..)",
        "",
        "    hop - next score (>>)",
        "    hop - previous score (<<)",
        "",
        "    log - aliases (al)",
        "    log - latex (lx)",
        "    log - lilypond (lp)",
        "",
        "    path - duplicate (dup)",
        "    path - get (get)",
        "    path - new (new)",
        "    path - remove (rm)",
        "    path - rename (ren)",
        "",
        "    score.pdf - open (spo)",
        "",
        "    shell - call (!)",
        "",
        "    show - column (;)",
        "    show - help (?)",
        "",
        "    text - edit (it)",
        "    text - replace (rp)",
        "    text - search (sr)",
        "",
    ]
