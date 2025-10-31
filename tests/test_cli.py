import subprocess
import sys

from repo_with_renovate import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "repo_with_renovate", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
