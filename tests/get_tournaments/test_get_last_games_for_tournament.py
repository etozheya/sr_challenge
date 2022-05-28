import pytest
import requests

import get_games
from tests import rnd_string, rnd_int


class MockResponse:
    def __init__(self, status_code=200):
        self._status_code = status_code

    @property
    def content(self):
        return b'{"mock_key": "mock_response"}'

    @property
    def status_code(self):
        return self._status_code


def test_get(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    monkeypatch.setattr(get_games, 'parse_games', lambda *_: 'games')
    result = get_games.get_last_games_for_tournament(rnd_string(), rnd_int())
    assert result == 'games'


def test_sr_error(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(status_code=500)

    monkeypatch.setattr(requests, 'get', mock_get)
    with pytest.raises(get_games.SRError):
        _ = get_games.get_last_games_for_tournament(
            rnd_string(), rnd_int())
