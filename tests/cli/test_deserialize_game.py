from cli_layer import cli
from tests import rnd_int, rnd_string


def test_full():
    game = {
        'round': rnd_int(),
        'timestamp': rnd_int(),
        'full_time_score': {'home': rnd_int(), 'away': rnd_int()},
        'half_time_score': {'home': rnd_int(), 'away': rnd_int()},
        'home_team_name': rnd_string(),
        'away_team_name': rnd_string(),
        'goals': [
            {
                'goalscorer_name': rnd_string(),
                'goal_minute': f'{rnd_int()}.',
                'new_score': f'{rnd_int()}:{rnd_int()}'}]}
    cli.deserialize_game(game, False)


def test_nil_nil():
    game = {
        'round': rnd_int(),
        'timestamp': rnd_int(),
        'full_time_score': {'home': 0, 'away': 0},
        'half_time_score': {'home': 0, 'away': 0},
        'home_team_name': rnd_string(),
        'away_team_name': rnd_string()}
    cli.deserialize_game(game, False)


def test_no_goals():
    game = {
        'round': rnd_int(),
        'timestamp': rnd_int(),
        'full_time_score': {'home': rnd_int(), 'away': rnd_int()},
        'half_time_score': {'home': rnd_int(), 'away': rnd_int()},
        'home_team_name': rnd_string(),
        'away_team_name': rnd_string()}
    cli.deserialize_game(game, False)


def test_morning_game():
    game = {
        'round': rnd_int(),
        'timestamp': 895042800,  # 1998-05-13 07:00
        'full_time_score': {'home': rnd_int(), 'away': rnd_int()},
        'half_time_score': {'home': rnd_int(), 'away': rnd_int()},
        'home_team_name': rnd_string(),
        'away_team_name': rnd_string(),
        'goals': [
            {
                'goalscorer_name': rnd_string(),
                'goal_minute': f'{rnd_int()}.',
                'new_score': f'{rnd_int()}:{rnd_int()}'}]}
    cli.deserialize_game(game, True)


def test_twelve_pm_game():
    game = {
        'round': rnd_int(),
        'timestamp': 895060800,  # 1998-05-13 12:00
        'full_time_score': {'home': rnd_int(), 'away': rnd_int()},
        'half_time_score': {'home': rnd_int(), 'away': rnd_int()},
        'home_team_name': rnd_string(),
        'away_team_name': rnd_string(),
        'goals': [
            {
                'goalscorer_name': rnd_string(),
                'goal_minute': f'{rnd_int()}.',
                'new_score': f'{rnd_int()}:{rnd_int()}'}]}
    cli.deserialize_game(game, True)


def test_afternoon_game():
    game = {
        'round': rnd_int(),
        'timestamp': 895068000,  # 1998-05-13 14:00
        'full_time_score': {'home': rnd_int(), 'away': rnd_int()},
        'half_time_score': {'home': rnd_int(), 'away': rnd_int()},
        'home_team_name': rnd_string(),
        'away_team_name': rnd_string(),
        'goals': [
            {
                'goalscorer_name': rnd_string(),
                'goal_minute': f'{rnd_int()}.',
                'new_score': f'{rnd_int()}:{rnd_int()}'}]}
    cli.deserialize_game(game, True)
