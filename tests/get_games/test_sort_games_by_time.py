from data_layer import get_games


def test_sort():
    games = [
        {'timestamp': 1638019807},
        {'timestamp': 1638019805},
        {'timestamp': 1638019809},
        {'timestamp': 1638019800},
        {'timestamp': 1638019801},
        {'timestamp': 1638019803}]
    sorted_games = get_games.sort_games_by_time(games)
    assert sorted_games == [
        {'timestamp': 1638019809},
        {'timestamp': 1638019807},
        {'timestamp': 1638019805},
        {'timestamp': 1638019803},
        {'timestamp': 1638019801},
        {'timestamp': 1638019800}
    ]
