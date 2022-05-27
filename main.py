import get_tournaments
from get_games import get_last_games_for_all_tournaments


def main(tournaments_input, number_of_games):
    # TODO check for input number
    available_tournaments = get_tournaments.get()
    # print('Here is a list of available tournaments:')
    # print([t['name'] for t in available_tournaments])
    tournaments = available_tournaments
    if tournaments_input:
        tournaments = []
        for ti in tournaments_input:
            found = [at for at in available_tournaments if at['name'] == ti]
            if not found:
                # print(f'You entered invalid tournament name: {ti}.')
                return
    games = get_last_games_for_all_tournaments(tournaments, number_of_games)
    # for g in games.values():
    #     print(g)
    return games


if __name__ == '__main__':
    main(None, 5)
