import get_tournaments
from get_games import get_last_games_for_all_tournaments


class UserInputError(Exception):
    ...


def main(tournaments_input, number_of_games):
    if number_of_games < 1:
        raise UserInputError('Non-positive number was entered')
    available_tournaments = get_tournaments.get()
    # print('Here is a list of available tournaments:')
    # print([t['name'] for t in available_tournaments])
    tournaments = available_tournaments
    if tournaments_input:
        tournaments = []
        for ti in tournaments_input:
            found = [at for at in available_tournaments if at['name'] == ti]
            tournaments.append(found[0])
            if not found:
                raise UserInputError(
                    f'You entered invalid tournament name: {ti}')
    games = get_last_games_for_all_tournaments(tournaments, number_of_games)
    return games
