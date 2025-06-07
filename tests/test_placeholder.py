import pathlib

def test_readme_exists():
    assert pathlib.Path('README.md').is_file()

def test_readme_contains_tagline():
    content = pathlib.Path('README.md').read_text()
    assert "*Building technology that helps humans flourish.*" in content
