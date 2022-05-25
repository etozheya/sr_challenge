import get_tournaments
from get_games import get_last_games_for_all_tournaments


def main():
    tournaments = get_tournaments.get()
    print('Here is a list of available tournaments:')
    print(list(tournaments.keys()))
    games = get_last_games_for_all_tournaments(tournaments[:2])
    for g in games.values():
        print(g)


if __name__ == '__main__':
    main()
