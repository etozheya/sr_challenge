import json

import requests


class SRError(Exception):
    ...


def get_last_games_for_all_tournaments(tournaments):
    last_games = {}
    for t in tournaments:
        tournament_id = t['_tid']
        last_games[t['name']] = get_last_games_for_tournament(tournament_id)
    return last_games


def get_last_games_for_tournament(tournament_id):
    url = f'https://cp.fn.sportradar.com/common/en/Etc:UTC/gismo/fixtures_tournament/{tournament_id}/2021'  # noqa
    rv = requests.get(url)
    if rv.status_code == 200:
        rv_stringified_json = rv.content.decode('utf8').replace("'", '"')
        return parse_games(json.loads(rv_stringified_json))
    else:
        print(f'Failed to get games: {rv.status_code}.')
    raise SRError('Failed to get games')


def parse_games(metadata):
    parsed_games = []
    for m in list(metadata['doc'][0]['data']['matches'].values()):
        parsed_games.append(serialize_game(m))
    return parsed_games[:5]


def serialize_game(game):
    """
    Only '_tld' and 'name' fields are passed further.
    Any other data is not valuable for the given task.
    """
    serialized = {}
    for k, v in game.items():
        if k in ('_tid', 'round'):
            serialized[k] = v
        if k == 'time':
            serialized['timestamp'] = v['uts']
    return serialized
