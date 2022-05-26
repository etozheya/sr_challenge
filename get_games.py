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
        games = parse_games(json.loads(rv.content))[:5]
        return games
    else:
        print(f'Failed to get games: {rv.status_code}.')
    raise SRError('Failed to get games')


def parse_games(metadata):
    parsed_games = []
    for m in list(metadata['doc'][0]['data']['matches'].values()):
        parsed_games.append(serialize_game(m))
    return sort_games_by_time(parsed_games)


def serialize_game(game):
    serialized = {}
    if game['canceled']:
        return None
    for k, v in game.items():
        if k in ('_tid', 'round'):
            serialized[k] = v
        if k == 'time':
            serialized['timestamp'] = v['uts']
        if k == 'result':
            serialized['full_time_score'] = {
                'home': v['home'], 'away': v['away']}
        if k == 'periods':
            if v is not None:  # some games don't have half-time data ¯\_(ツ)_/¯
                serialized['half_time_score'] = v['p1']
        if k == 'teams':
            serialized['home_team_name'] = v['home']['name']
            serialized['away_team_name'] = v['away']['name']
        if k == 'comment':
            serialized['goals'] = serialize_comment(v)
    return serialized


def serialize_comment(comment):
    serialized = []
    if not comment:
        return None
    goals = comment.split(', ')
    for goal in goals:
        serialized_goal = {}
        goal_data = goal.split(' ')
        serialized_goal['goalscorer_name'] = goal_data[2]
        serialized_goal['goal_minute'] = (goal_data[1])[1:-1]
        serialized_goal['new_score'] = goal_data[0]
        serialized.append(serialized_goal)
    return serialized


def sort_games_by_time(games):
    """
    Function returns list of games from newest to oldest.
    """
    non_cancelled = [g for g in games if g]
    return sorted(non_cancelled, key=lambda g: g['timestamp'], reverse=True)
