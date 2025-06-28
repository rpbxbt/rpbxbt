import subprocess
import sys


def test_cli_output():
    result = subprocess.run(
        [sys.executable, '-m', 'nexus_ai.cli', 'data/nexus_sample_data.json'],
        capture_output=True,
        text=True,
        check=True,
    )
    expected = (
        "Nodes: Alpha, Beta, Gamma, Delta\n"
        "Network score: 0.67\n"
    )
    assert result.stdout == expected
