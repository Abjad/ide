import abjad
import ide
abjad_ide = ide.AbjadIDE(test=True)


def test_AbjadIDE_new_01():
    """
    Makes build directory.
    """

    build = ide.Path('red_score', 'builds', 'arch-a-score')
    with ide.Test(remove=[build]):

        abjad_ide('red bb new score arch-a-score arch~a $80 ARCH-A y q')
        transcript = abjad_ide.io.transcript
        lines = transcript.lines
        assert build.is_dir()
        assert build.get_metadatum('price') == '$80'
        assert build.get_metadatum('catalog_number_suffix') == 'ARCH-A'
        assert 'Build name> arch-a-score' in lines
        assert 'Paper size> arch a' in lines
        assert r'Price> $80' in lines
        assert 'Catalog number suffix> ARCH-A'in lines
        index = lines.index('Ok?> y')
        assert lines[index:] == [
            'Ok?> y',
            '',
            'Writing red_score/builds/arch-a-score/back-cover.tex ...',
            '',
            'Writing red_score/builds/arch-a-score/front-cover.tex ...',
            '',
            'Writing red_score/builds/arch-a-score/layout.py ...',
            '',
            'Collecting segment lys ...',
            ' Writing red_score/builds/arch-a-score/_segments/segment--.ily ...',
            ' Writing red_score/builds/arch-a-score/_segments/segment--.ly ...',
            ' Writing red_score/builds/arch-a-score/_segments/segment-A.ily ...',
            ' Writing red_score/builds/arch-a-score/_segments/segment-A.ly ...',
            ' Writing red_score/builds/arch-a-score/_segments/segment-B.ily ...',
            ' Writing red_score/builds/arch-a-score/_segments/segment-B.ly ...',
            'Handling edition tags ...',
            ' Found no other-edition tags ...',
            ' Found no this-edition tags ...',
            'Handling fermata bar lines ...',
            ' Found no bar line adjustment tags ...',
            'Handling shifted clefs ...',
            ' Found no shifted clef tags ...',
            'Uncoloring persistent indicators ...',
            ' Found no persistent indicator color suppression tags ...',
            ' Found no persistent indicator color expression tags ...',
            'Hiding default clefs ...',
            ' Found no default clef tags ...',
            'Hiding music annotations ...',
            ' Found no music annotation tags ...',
            'Joining broken spanners ...',
            ' Found no broken spanner expression tags ...',
            ' Found no broken spanner suppression tags ...',
            'Hiding PHANTOM tags ...',
            ' Found no PHANTOM tags ...',
            '',
            'Generating red_score/builds/arch-a-score/music.ly ...',
            ' Examining red_score/segments/_ ...',
            ' Examining red_score/segments/A ...',
            ' Examining red_score/segments/B ...',
            ' Writing red_score/builds/arch-a-score/music.ly ...',
            '',
            'Writing red_score/builds/arch-a-score/preface.tex ...',
            '',
            'Generating score ...',
            'Writing red_score/builds/arch-a-score/score.tex ...',
            '',
            'Generating stylesheet ...',
            'Writing red_score/builds/arch-a-score/stylesheet.ily ...',
            '',
            '> q',
            '',
            ]

        abjad_ide('red bb new score arch-a-score q')
        transcript = abjad_ide.io.transcript
        assert f'Existing {build.trim()} ...' in transcript


def test_AbjadIDE_new_02():
    """
    Makes build directory. Ignores empty metadata.
    """

    path = ide.Path('red_score', 'builds', 'arch-a-score')
    with ide.Test(remove=[path]):

        abjad_ide('red bb new score arch-a-score arch~a <return> <return> y q')
        transcript = abjad_ide.io.transcript
        assert path.is_dir()
        assert path.get_metadatum('price') is None
        assert path.get_metadatum('catalog_number_suffix') is None
        assert 'Build name> arch-a-score' in transcript
        assert 'Paper size> arch a' in transcript
        assert r'Price>' in transcript
        assert 'Catalog number suffix>'in transcript
        assert 'Making ...' in transcript
        assert f'    {path.trim()}' in transcript
        paths = [path / _ for _ in (
            'back-cover.tex',
            'front-cover.tex',
            'music.ly',
            'preface.tex',
            'score.tex',
            'stylesheet.ily',
            )]
        for path in paths:
            assert f'    {path.trim()}' in transcript
        assert 'Ok?> y' in transcript
        assert 'Generating score ...' in transcript
        assert 'Generating stylesheet ...' in transcript
        for path in paths:
            assert f'Writing {path.trim()} ...' in transcript


def test_AbjadIDE_new_03():
    """
    Makes material package.
    """

    path = ide.Path('red_score', 'materials', 'test_notes')
    with ide.Test(remove=[path]):

        abjad_ide('red mm new test~notes q')
        transcript = abjad_ide.io.transcript
        assert path.is_dir()
        names = [
            '__init__.py',
            'definition.py',
            ]
        for name in names:
            assert (path / name).is_file()
        assert 'Enter package name> test notes' in transcript
        assert f'Making {path.trim()} ...' in transcript
        for name in names:
            assert f'Writing {(path / name).trim()} ...' in transcript

        abjad_ide('red mm new test_notes q')
        transcript = abjad_ide.io.transcript
        assert f'Existing {path.trim()} ...'


def test_AbjadIDE_new_04():
    """
    Makes parts directory.
    """

    with ide.Test():
        directory = ide.Path('green_score', 'builds', 'arch-a-parts')
        assert not directory.exists()

        abjad_ide('gre bb new parts arch-a-parts arch~a ARCH-A y q')
        transcript = abjad_ide.io.transcript
        lines = transcript.lines
        assert 'Getting part names from score template ...' in lines
        assert 'Found BassClarinet ...' in lines
        assert 'Found Violin ...' in lines
        assert 'Found Viola ...' in lines
        assert 'Found Cello ...' in lines

        assert 'Directory name> arch-a-parts' in lines
        assert 'Paper size> arch a' in lines
        assert 'Catalog number suffix> ARCH-A' in lines
        assert 'Will make ...' in lines
        for line in [
            '    green_score/builds/arch-a-parts',
            '    green_score/builds/arch-a-parts/stylesheet.ily',
            '    green_score/builds/arch-a-parts/bass-clarinet/bass-clarinet-front-cover.tex',
            '    green_score/builds/arch-a-parts/bass-clarinet/bass-clarinet-preface.tex',
            '    green_score/builds/arch-a-parts/bass-clarinet/bass-clarinet-music.ly',
            '    green_score/builds/arch-a-parts/bass-clarinet/bass-clarinet-back-cover.tex',
            '    green_score/builds/arch-a-parts/bass-clarinet/bass-clarinet-part.tex',
            '    green_score/builds/arch-a-parts/violin/violin-front-cover.tex',
            '    green_score/builds/arch-a-parts/violin/violin-preface.tex',
            '    green_score/builds/arch-a-parts/violin/violin-music.ly',
            '    green_score/builds/arch-a-parts/violin/violin-back-cover.tex',
            '    green_score/builds/arch-a-parts/violin/violin-part.tex',
            '    green_score/builds/arch-a-parts/viola/viola-front-cover.tex',
            '    green_score/builds/arch-a-parts/viola/viola-preface.tex',
            '    green_score/builds/arch-a-parts/viola/viola-music.ly',
            '    green_score/builds/arch-a-parts/viola/viola-back-cover.tex',
            '    green_score/builds/arch-a-parts/viola/viola-part.tex',
            '    green_score/builds/arch-a-parts/cello/cello-front-cover.tex',
            '    green_score/builds/arch-a-parts/cello/cello-preface.tex',
            '    green_score/builds/arch-a-parts/cello/cello-music.ly',
            '    green_score/builds/arch-a-parts/cello/cello-back-cover.tex',
            '    green_score/builds/arch-a-parts/cello/cello-part.tex',
            ]:
            assert line in lines, repr(line)

        assert 'Ok?> y' in lines

        for line in [
            'Ok?> y',
            'Collecting segment lys ...',
            ' Writing green_score/builds/arch-a-parts/_segments/segment--.ly ...',
            'Uncoloring persistent indicators ...',
            ' Found 1 persistent indicator color suppression tag ...',
            ' Activating 1 persistent indicator color suppression tag ...',
            ' Found 30 persistent indicator color expression tags ...',
            ' Deactivating 26 persistent indicator color expression tags ...',
            ' Skipping 4 (inactive) persistent indicator color expression tags ...',
            'Hiding music annotations ...',
            ' Found 3 music annotation tags ...',
            ' Deactivating 1 music annotation tag ...',
            ' Skipping 2 (inactive) music annotation tags ...',
            'Generating stylesheet ...',
            'Writing green_score/builds/arch-a-parts/stylesheet.ily ...',
            'Writing green_score/builds/arch-a-parts/bass-clarinet/bass-clarinet-back-cover.tex ...',
            'Writing green_score/builds/arch-a-parts/bass-clarinet/bass-clarinet-front-cover.tex ...',
            'Writing green_score/builds/arch-a-parts/bass-clarinet/bass-clarinet-music.ly ...',
            'Writing green_score/builds/arch-a-parts/bass-clarinet/bass-clarinet-part.tex ...',
            'Writing green_score/builds/arch-a-parts/bass-clarinet/bass-clarinet-preface.tex ...',
            'Writing green_score/builds/arch-a-parts/bass-clarinet/bass_clarinet_layout.py ...',
            'Writing green_score/builds/arch-a-parts/violin/violin-back-cover.tex ...',
            'Writing green_score/builds/arch-a-parts/violin/violin-front-cover.tex ...',
            'Writing green_score/builds/arch-a-parts/violin/violin-music.ly ...',
            'Writing green_score/builds/arch-a-parts/violin/violin-part.tex ...',
            'Writing green_score/builds/arch-a-parts/violin/violin-preface.tex ...',
            'Writing green_score/builds/arch-a-parts/violin/violin_layout.py ...',
            'Writing green_score/builds/arch-a-parts/viola/viola-back-cover.tex ...',
            'Writing green_score/builds/arch-a-parts/viola/viola-front-cover.tex ...',
            'Writing green_score/builds/arch-a-parts/viola/viola-music.ly ...',
            'Writing green_score/builds/arch-a-parts/viola/viola-part.tex ...',
            'Writing green_score/builds/arch-a-parts/viola/viola-preface.tex ...',
            'Writing green_score/builds/arch-a-parts/viola/viola_layout.py ...',
            'Writing green_score/builds/arch-a-parts/cello/cello-back-cover.tex ...',
            'Writing green_score/builds/arch-a-parts/cello/cello-front-cover.tex ...',
            'Writing green_score/builds/arch-a-parts/cello/cello-music.ly ...',
            'Writing green_score/builds/arch-a-parts/cello/cello-part.tex ...',
            'Writing green_score/builds/arch-a-parts/cello/cello-preface.tex ...',
            'Writing green_score/builds/arch-a-parts/cello/cello_layout.py ...',
            '',
            '> q',
            '',
            ]:
            assert line in lines, repr(line)

        assert directory.is_parts()
        assert (directory / '__metadata__.py').is_file()
        assert directory._assets.exists()
        assert (directory._assets / '.gitignore').is_file()
        assert directory._segments.exists()
        assert (directory._segments / '.gitignore').is_file()
        assert (directory._segments / 'segment--.ly').is_file()

        for name in [
            'bass-clarinet-back-cover.tex',
            'bass-clarinet-front-cover.tex',
            'bass-clarinet-music.ly',
            'bass-clarinet-part.tex',
            'bass-clarinet-preface.tex',
            'bass_clarinet_layout.py',
            ]:
            path = directory / 'bass-clarinet' / name
            assert path.is_file()

        for name in [
            'cello-back-cover.tex',
            'cello-front-cover.tex',
            'cello-music.ly',
            'cello-part.tex',
            'cello-preface.tex',
            'cello_layout.py',
            ]:
            path = directory / 'cello' / name
            assert path.is_file()

        for name in [
            'viola-back-cover.tex',
            'viola-front-cover.tex',
            'viola-music.ly',
            'viola-part.tex',
            'viola-preface.tex',
            'viola_layout.py',
            ]:
            path = directory / 'viola' / name
            assert path.is_file()

        for name in [
            'violin-back-cover.tex',
            'violin-front-cover.tex',
            'violin-music.ly',
            'violin-part.tex',
            'violin-preface.tex',
            'violin_layout.py',
            ]:
            path = directory / 'violin' / name
            assert path.is_file(), repr(path)

        stylesheet = directory / 'stylesheet.ily'
        assert stylesheet.is_file()


def test_AbjadIDE_new_05():
    """
    Makes score package.
    """

    with ide.Test():

        abjad_ide('new Purple~Score q')
        transcript = abjad_ide.io.transcript
        wrapper = ide.Path('test_scores') / 'purple_score'
        assert wrapper.is_dir()
        for name in [
            '.gitignore',
            '.travis.yml',
            'README.md',
            'purple_score',
            'requirements.txt',
            'setup.cfg',
            'setup.py',
            ]:
            assert (wrapper / name).exists()
        for name in [
            '__init__.py',
            '__metadata__.py',
            'builds',
            'distribution',
            'etc',
            'materials',
            'segments',
            'stylesheets',
            'test',
            'tools',
            ]:
            assert (wrapper.contents / name).exists()
        assert (wrapper.materials / '__init__.py').is_file()
        assert (wrapper.segments / '__init__.py').is_file()
        assert 'Enter title> Purple Score' in transcript
        assert f'Making {wrapper.trim()} ...' in transcript

        assert wrapper.builds._assets.exists()
        assert (wrapper.builds._assets / '.gitignore').is_file()
        assert (wrapper.builds / '__metadata__.py').is_file()

        abjad_ide('new Purple~Score q')
        transcript = abjad_ide.io.transcript
        assert f'Existing {wrapper.trim()} ...' in transcript


def test_AbjadIDE_new_06():
    """
    Makes score package in empty directory.
    """

    with ide.Test():
        wrapper = ide.Path('test_scores') / 'purple_score'
        wrapper.remove()
        wrapper.mkdir()
        assert wrapper.is_dir()
        git = wrapper / '.git'
        git.mkdir()
        assert git.is_dir()

        abjad_ide('new y Purple~Score q')
        transcript = abjad_ide.io.transcript
        assert wrapper.exists()
        for name in [
            '.travis.yml',
            'README.md',
            'requirements.txt',
            'setup.cfg',
            'setup.py',
            ]:
            assert (wrapper / name).exists()
        for name in [
            '__init__.py',
            '__metadata__.py',
            'builds',
            'distribution',
            'etc',
            'tools',
            'materials',
            'segments',
            'stylesheets',
            'test',
            ]:
            assert (wrapper.contents/ name).exists()
        assert (wrapper.materials / '__init__.py').is_file()
        assert (wrapper.segments / '__init__.py').is_file()
        assert f'Found {wrapper.trim()}.' in transcript
        assert f'Populate {wrapper.trim()}?>' in transcript
        assert 'Enter title> Purple Score' in transcript
        assert f'Making {wrapper.trim()} ...' in transcript

        abjad_ide('new Purple~Score q')
        transcript = abjad_ide.io.transcript
        assert f'Existing {wrapper.trim()} ...' in transcript


def test_AbjadIDE_new_07():
    """
    Makes score package. Coerces package name.
    """

    package = ide.Path('test_scores') / 'purple_score'

    with ide.Test(remove=[package]):

        abjad_ide('new PurpleScore q')
        assert package.is_dir()

    with ide.Test(remove=[package]):

        abjad_ide('new purpleScore q')
        assert package.is_dir()

    with ide.Test(remove=[package]):

        abjad_ide('new Purple_Score q')
        assert package.is_dir()

    with ide.Test(remove=[package]):

        abjad_ide('new purple_score q')
        assert package.is_dir()


def test_AbjadIDE_new_08():
    """
    Makes segment directory.
    """

    path = ide.Path('red_score', 'segments', 'segment_04')
    with ide.Test(remove=[path]):

        abjad_ide('red gg new segment~04 q')
        transcript = abjad_ide.io.transcript
        assert path.is_dir()
        names = [
            '__init__.py',
            '__metadata__.py',
            'definition.py',
            'layout.py',
            ]
        for name in names:
            assert (path / name).is_file()
        assert 'Enter package name> segment 04' in transcript
        assert f'Making {path.trim()} ...' in transcript
        for name in names:
            assert f'Writing {(path / name).trim()} ...' in transcript

        abjad_ide('red gg new segment_04 q')
        transcript = abjad_ide.io.transcript
        assert f'Existing {path.trim()} ...'


def test_AbjadIDE_new_09():
    """
    Makes stylesheet.
    """

    path = ide.Path('red_score', 'stylesheets', 'new-stylesheet.ily')
    with ide.Test(remove=[path]):

        abjad_ide('red yy new new~stylesheet y q')
        transcript = abjad_ide.io.transcript
        assert path.is_file()
        assert 'File name> new stylesheet' in transcript
        assert f'Writing {path.trim()} ...' in transcript
        assert 'Ok?> y' in transcript

        abjad_ide('red yy new new~stylesheet.ily q')
        transcript = abjad_ide.io.transcript
        assert f'Existing {path.trim()} ...'

        abjad_ide('red yy new <return> q')
        transcript = abjad_ide.io.transcript
        assert 'Existing' not in transcript
        assert 'Writing' not in transcript

        abjad_ide('red yy new ss q')
        transcript = abjad_ide.io.transcript
        assert 'Existing' not in transcript
        assert 'Writing' not in transcript


def test_AbjadIDE_new_10():
    """
    Makes tools classfile.
    """

    path = ide.Path('red_score', 'tools', 'NewClass.py')
    with ide.Test(remove=[path]):

        abjad_ide('red oo new NewClass.py y q')
        transcript = abjad_ide.io.transcript
        assert path.is_file()
        text = path.read_text()
        assert 'class NewClass(object)' in text
        assert 'File name> NewClass' in transcript
        assert f'Writing {path.trim()} ...' in transcript
        assert 'Ok?> y' in transcript

        abjad_ide('red oo new NewClass q')
        transcript = abjad_ide.io.transcript
        assert f'Existing {path.trim()} ...'


def test_AbjadIDE_new_11():
    """
    Makes tools functionfile.
    """

    path = ide.Path('red_score', 'tools', 'make_material.py')
    with ide.Test(remove=[path]):

        abjad_ide('red oo new make_material y q')
        transcript = abjad_ide.io.transcript
        assert path.is_file()
        text = path.read_text()
        assert 'def make_material():' in text
        assert 'File name> make_material' in transcript
        assert f'Writing {path.trim()} ...' in transcript
        assert 'Ok?> y' in transcript

        abjad_ide('red oo new make~material q')
        transcript = abjad_ide.io.transcript
        assert f'Existing {path.trim()} ...'


def test_AbjadIDE_new_12():
    """
    In library.
    """

    if not abjad.abjad_configuration.composer_library_tools:
        return

    directory = ide.Path(abjad.abjad_configuration.composer_library_tools)
    with abjad.FilesystemState(keep=[directory]):

        abjad_ide('ll new FooCommand y q')
        transcript = abjad_ide.io.transcript
        path = directory / 'FooCommand.py'
        assert path.is_file()
        assert 'File name> FooCommand' in transcript
        assert f'Writing {path.trim()} ...' in transcript
        assert 'Ok?> y' in transcript

        abjad_ide('ll new FooCommand q')
        transcript = abjad_ide.io.transcript
        assert f'Existing {path.trim()} ...' in transcript

        abjad_ide('ll new foo~command y q')
        transcript = abjad_ide.io.transcript
        path = directory / 'foo_command.py'
        assert path.is_file()
        assert 'File name> foo command' in transcript
        assert f'Writing {path.trim()} ...' in transcript
        assert 'Ok?> y' in transcript

        abjad_ide('ll new foo~command q')
        transcript = abjad_ide.io.transcript
        assert f'Existing {path.trim()} ...' in transcript