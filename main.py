import get_tournaments
from get_games import get_last_games_for_all_tournaments


def main():
    tournaments = get_tournaments.get()
    print('Here is a list of available tournaments:')
    print([t['_tid'] for t in tournaments])
    games = get_last_games_for_all_tournaments(tournaments)
    for g in games.values():
        print(g)


if __name__ == '__main__':
    main()
