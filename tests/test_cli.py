import subprocess
import sys


def test_cli_output():
    result = subprocess.run(
        [sys.executable, '-m', 'belonging.cli', 'data/sample_data.json'],
        capture_output=True,
        text=True,
        check=True,
    )
    expected = (
        "Members: Alice, Bob, Charlie, Dana\n"
        "Belonging score: 0.67\n"
    )
    assert result.stdout == expected
