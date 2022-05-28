from data_layer import data
import pytest


def test_not_custom(monkeypatch):
    tournaments = [{'name': 'bl'}, {'name': 'blc'}]
    monkeypatch.setattr(data.get_tournaments, 'get', lambda *_: tournaments)
    monkeypatch.setattr(
        data, 'get_last_games_for_all_tournaments', lambda *_: 'games')
    games = data.main(None, 5)
    assert games == 'games'


def test_custom(monkeypatch):
    tournaments = [{'name': 'bl'}, {'name': 'blc'}]
    monkeypatch.setattr(data.get_tournaments, 'get', lambda *_: tournaments)
    monkeypatch.setattr(
        data, 'get_last_games_for_all_tournaments', lambda *_: 'games')
    games = data.main(['bl'], 5)
    assert games == 'games'


def test_invalid_tournament_name(monkeypatch):
    tournaments = [{'name': 'bl'}, {'name': 'blc'}]
    monkeypatch.setattr(data.get_tournaments, 'get', lambda *_: tournaments)
    monkeypatch.setattr(
        data, 'get_last_games_for_all_tournaments', lambda *_: 'games')
    with pytest.raises(data.UserInputError):
        _ = data.main(['qwer'], 5)


def test_invalid_number_of_games(monkeypatch):
    tournaments = [{'name': 'bl'}, {'name': 'blc'}]
    monkeypatch.setattr(data.get_tournaments, 'get', lambda *_: tournaments)
    monkeypatch.setattr(
        data, 'get_last_games_for_all_tournaments', lambda *_: 'games')
    with pytest.raises(data.UserInputError):
        _ = data.main(['qwer'], 0)
