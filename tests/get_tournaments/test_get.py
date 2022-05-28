import pytest
import requests

from data_layer import get_tournaments


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
    monkeypatch.setattr(
        get_tournaments, 'parse_tournaments', lambda *_: 'tournaments')
    result = get_tournaments.get()
    assert result == 'tournaments'


def test_sr_error(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(status_code=500)

    monkeypatch.setattr(requests, 'get', mock_get)
    with pytest.raises(get_tournaments.SRError):
        _ = get_tournaments.get()
