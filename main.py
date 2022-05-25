import json

import requests


class SRError(Exception):
    ...


def get_tournaments():
    url = 'https://cp.fn.sportradar.com/common/en/Etc:UTC/gismo/config_tournaments/1/17'  # noqa
    rv = requests.get(url)
    if rv.status_code == 200:
        rv_stringified_json = rv.content.decode('utf8').replace("'", '"')
        return parse_tournaments(json.loads(rv_stringified_json))
    else:
        print(f'Failed to get tournaments: {rv.status_code}.')
    raise SRError('Failed to get tournaments')


def parse_tournaments(metadata):
    parsed_tournaments = []
    for t in metadata['doc'][0]['data']['tournaments']:
        parsed_tournaments.append(serialize_tournament(t))
    return parsed_tournaments


def serialize_tournament(tournament):
    serialized = {}
    for k, v in tournament.items():
        if k in ('_tid', 'name'):
            serialized[k] = v
    return serialized


def get_last_games_for_all_tournaments(tournaments):
    for t in tournaments.values():
        tournament_id = t['_tid']
        get_last_games_for_tournament(tournament_id)
    pass


def get_last_games_for_tournament(tournament_id):
    pass


def main():
    tournaments = get_tournaments()
    # print('Here is a list of available tournaments:')
    # print(list(tournaments.keys()))
    # _ = get_last_games_for_all_tournaments(tournaments)
    print(tournaments)


if __name__ == '__main__':
    main()
