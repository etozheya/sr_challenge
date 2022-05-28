from data_layer import get_tournaments
from data_layer.get_games import get_last_games_for_all_tournaments


class UserInputError(Exception):
    ...


def main(tournaments_input, number_of_games):
    if number_of_games < 1:
        raise UserInputError('Non-positive number was entered')
    available_tournaments = get_tournaments.get()
    tournaments = available_tournaments
    if tournaments_input:
        tournaments = []
        for ti in tournaments_input:
            found = [at for at in available_tournaments if at['name'] == ti]
            if not found:
                raise UserInputError(
                    f'You entered invalid tournament name: {ti}')
            tournaments.append(found[0])
    games = get_last_games_for_all_tournaments(tournaments, number_of_games)
    return games
