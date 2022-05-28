import get_tournaments
from tests import rnd_string, rnd_int


def test_serialize(monkeypatch):
    tournament = {
        rnd_string(): rnd_string(),
        '_tid': rnd_int(),
        rnd_string(): rnd_string(),
        'name': rnd_string(),
        rnd_string(): rnd_string()}
    serialized = get_tournaments.serialize_tournament(tournament)
    assert list(serialized.keys()) == ['_tid', 'name']
