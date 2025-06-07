import pathlib

def test_readme_exists():
    assert pathlib.Path('README.md').is_file()
