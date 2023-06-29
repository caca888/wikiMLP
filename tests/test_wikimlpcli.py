from src.wikimlpcli import cli
from click.testing import CliRunner

runner = CliRunner()

def test_cli_phrase():
    response = runner.invoke(cli, ["-f", "phrase", "-n", "Germany"])
    assert response.exit_code == 0
    assert "germany" in response.output

def test_cli_summary():
    response = runner.invoke(cli, ["-f", "summary", "-n", "Germany"])
    assert response.exit_code == 0
    assert 'Germany, officially the Federal Republic of Germany,' in response.output

def test_cli_failed():
    response = runner.invoke(cli, [])
    assert response.exit_code != 0
    assert "Usage: cli [OPTIONS]\nTry 'cli --help' for help.\n\nError: Missing option '-f' / '--func'. Choose from:\n\tphrase,\n\tsummary\n" in response.output