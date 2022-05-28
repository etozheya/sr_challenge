import data


def test_not_custom(monkeypatch):
    tournaments = [{'name': 'bl'}, {'name': 'blc'}]
    monkeypatch.setattr(main.get_tournaments, 'get', lambda *_: tournaments)
    monkeypatch.setattr(
        main, 'get_last_games_for_all_tournaments', lambda *_: 'games')
    games = main.main(None, 5)
    assert games == 'games'


def test_custom(monkeypatch):
    tournaments = [{'name': 'bl'}, {'name': 'blc'}]
    monkeypatch.setattr(main.get_tournaments, 'get', lambda *_: tournaments)
    monkeypatch.setattr(
        main, 'get_last_games_for_all_tournaments', lambda *_: 'games')
    games = main.main(['bl'], 5)
    assert games == 'games'


def test_invalid_tournament_name(monkeypatch):
    tournaments = [{'name': 'bl'}, {'name': 'blc'}]
    monkeypatch.setattr(main.get_tournaments, 'get', lambda *_: tournaments)
    monkeypatch.setattr(
        main, 'get_last_games_for_all_tournaments', lambda *_: 'games')
    games = main.main(['qwer'], 5)
    assert not games
