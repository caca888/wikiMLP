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
    assert "Usage: cli [OPTIONS]" in response.output

def test_cli_conclude():
    response = runner.invoke(cli, ["-f", "conclude", "-n", "Germany"])
    assert response.exit_code == 0
    assert 'Germany, officially the Federal Republic of Germany,' in response.output

def test_cli_sentiment():
    response = runner.invoke(cli, ["-f", "sentiment", "-n", "Germany"])
    assert response.exit_code == 0
    assert '1) positive 0.672' in response.output