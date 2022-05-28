from data_layer import get_games


def test_parse(monkeypatch):
    metadata = {'doc': [{'data': {'matches': {'_': '_', '__': '__'}}}]}
    monkeypatch.setattr(get_games, 'serialize_game', lambda *_: 'serialized')
    monkeypatch.setattr(
        get_games, 'sort_games_by_time', lambda *_: 'sorted')
    parsed_games = get_games.parse_games(metadata)
    assert parsed_games == 'sorted'
