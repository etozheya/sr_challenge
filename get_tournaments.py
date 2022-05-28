import json

import requests


class SRError(Exception):
    ...


def get():
    url = 'https://cp.fn.sportradar.com/common/en/Etc:UTC/gismo/config_tournaments/1/17'  # noqa
    rv = requests.get(url)
    if rv.status_code == 200:
        rv_stringified_json = rv.content.decode('utf8').replace("'", '"')
        return parse_tournaments(json.loads(rv_stringified_json))
    else:
        raise SRError('Failed to get tournaments')


def parse_tournaments(metadata):
    """
    Only 'tournaments' are taken into account here.
    API with 'uniquetournaments' id-s do not provide any match data.
    """
    parsed_tournaments = []
    for t in metadata['doc'][0]['data']['tournaments']:
        parsed_tournaments.append(serialize_tournament(t))
    return parsed_tournaments


def serialize_tournament(tournament):
    """
    Only '_tld' and 'name' fields are passed further.
    Any other data is not valuable for the given task.
    """
    serialized = {}
    for k, v in tournament.items():
        if k in ('_tid', 'name'):
            serialized[k] = v
    return serialized
