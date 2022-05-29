from cli_layer import cli
from tests import rnd_string, rnd_int


def test_get(monkeypatch):
    first_tournament = rnd_string()
    second_tournament = rnd_string()
    tournaments = [
        {'_tid': rnd_int(), 'name': first_tournament},
        {'_tid': rnd_int(), 'name': second_tournament}]
    monkeypatch.setattr(cli.get_tournaments, 'get', lambda *_: tournaments)
    available_tournaments = cli.get_available_tournaments()
    assert available_tournaments == [first_tournament, second_tournament]
