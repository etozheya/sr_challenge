from data_layer import get_games
from tests import rnd_int, rnd_string


def test_empty():
    serialized = get_games.serialize_comment(None)
    assert serialized is None


def test_non_empty(monkeypatch):
    first_goalscorer = rnd_string()
    second_goalscorer = rnd_string()
    first_goal_minute = rnd_int()
    second_goal_minute = rnd_int()
    comment = f'1:0 ({first_goal_minute}.) {first_goalscorer},' \
              f' 1:1 ({second_goal_minute}.) {second_goalscorer} (pen)'
    serialized = get_games.serialize_comment(comment)
    assert serialized == [
        {
            'goalscorer_name': first_goalscorer,
            'goal_minute': f'{first_goal_minute}.',
            'new_score': '1:0'
        },
        {
            'goalscorer_name': second_goalscorer,
            'goal_minute': f'{second_goal_minute}.',
            'new_score': '1:1'
        }]
