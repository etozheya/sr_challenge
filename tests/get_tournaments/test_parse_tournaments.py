from data_layer import get_tournaments


def test_parse(monkeypatch):
    metadata = {'doc': [{'data': {'tournaments': {'_': '_', '__': '__'}}}]}
    monkeypatch.setattr(
        get_tournaments, 'serialize_tournament', lambda *_: 'serialized')
    parsed_games = get_tournaments.parse_tournaments(metadata)
    assert parsed_games == ['serialized' for _ in range(2)]
