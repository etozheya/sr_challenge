import get_games
from tests import rnd_string, rnd_int


def test_get(monkeypatch):
    tournaments = [{'_tid': rnd_int(), 'name': rnd_string()} for _ in range(20)]
    monkeypatch.setattr(
        get_games, 'get_last_games_for_tournament', lambda *_: 'game')
    last_games = get_games.get_last_games_for_all_tournaments(tournaments, 10)
    assert len(last_games) == 20
    assert last_games[tournaments[0]['name']] == 'game'
