from cli_layer import cli
from click.testing import CliRunner


def test_cli(monkeypatch):
    monkeypatch.setattr(cli.data, 'main', lambda *_: games)
    monkeypatch.setattr(cli, 'deserialize_game', lambda *_: 'deserialized')
    runner = CliRunner()
    # result = runner.invoke(cli)
    pass
