import get_games
from tests import rnd_int, rnd_string


def test_cancelled():
    game = {'canceled': True}
    serialized = get_games.serialize_game(game)
    assert serialized is None


def test_not_cancelled(monkeypatch):
    game = {
        'canceled': False,
        '_tid': rnd_int(),
        'round': rnd_string(),
        'time': {'uts': str(rnd_int())},
        'result': {'home': rnd_int(), 'away': rnd_int()},
        'periods': {'p1': {'home': rnd_int(), 'away': rnd_int()}},
        'teams': {
            'home': {'name': rnd_string()}, 'away': {'name': rnd_string()}},
        'comment': rnd_string()}
    monkeypatch.setattr(get_games, 'serialize_comment', lambda *_: 'goals')
    serialized = get_games.serialize_game(game)
    assert serialized == {
        '_tid': game['_tid'],
        'round': game['round'],
        'timestamp': game['time']['uts'],
        'full_time_score': {
            'home': game['result']['home'], 'away': game['result']['away']},
        'half_time_score': {
            'home': game['periods']['p1']['home'],
            'away': game['periods']['p1']['away']},
        'home_team_name': game['teams']['home']['name'],
        'away_team_name': game['teams']['away']['name'],
        'goals': 'goals'}


def test_no_half_time_data(monkeypatch):
    game = {
        'canceled': False,
        '_tid': rnd_int(),
        'round': rnd_string(),
        'time': {'uts': str(rnd_int())},
        'result': {'home': rnd_int(), 'away': rnd_int()},
        'periods': None,
        'teams': {
            'home': {'name': rnd_string()}, 'away': {'name': rnd_string()}},
        'comment': rnd_string()}
    monkeypatch.setattr(get_games, 'serialize_comment', lambda *_: 'goals')
    serialized = get_games.serialize_game(game)
    assert serialized == {
        '_tid': game['_tid'],
        'round': game['round'],
        'timestamp': game['time']['uts'],
        'full_time_score': {
            'home': game['result']['home'], 'away': game['result']['away']},
        'home_team_name': game['teams']['home']['name'],
        'away_team_name': game['teams']['away']['name'],
        'goals': 'goals'}

