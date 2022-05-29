from cli_layer import cli
from click.testing import CliRunner
from data_layer.get_games import SRError
from tests import rnd_string


def test_cli(monkeypatch):
    games = {rnd_string(): rnd_string() for _ in range(10)}
    monkeypatch.setattr(cli.data, 'main', lambda *_: games)
    monkeypatch.setattr(cli, 'deserialize_game', lambda *_: 'deserialized')
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'last 5 games' in result.output


def test_unexpected_error(monkeypatch):
    def mocked_raise(e):
        raise e

    monkeypatch.setattr(cli.data, 'main', lambda *_: mocked_raise(SRError))
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 1
    assert 'Unexpected error' in result.output
