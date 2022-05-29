#!/usr/bin/env python
import sys
import os
from pathlib import Path
from datetime import datetime

import click

from data_layer import data, get_tournaments


myDir = os.getcwd()
sys.path.append(myDir)
path = Path(myDir)
a = str(path.parent.absolute())
sys.path.append(a)


def deserialize_game(game, is_am_pm_format):
    time = str(datetime.utcfromtimestamp(game["timestamp"]))[:-3]
    if is_am_pm_format:
        hours = int(time[11:13])
        if hours > 11:
            if hours > 12:
                time = time[:11] + str(hours - 12) + time[13:] + ' PM'
            else:
                time += ' PM'
        else:
            time += ' AM'
    click.echo(f'Round {game["round"]}. {time}')
    click.echo(
        f'{game["home_team_name"]} : {game["away_team_name"]} -'
        f' {game["full_time_score"]["home"]}:{game["full_time_score"]["away"]}'
        f' ({game["half_time_score"]["home"]}:{game["half_time_score"]["away"]}'
        f')')
    if game.get('goals'):
        for goal in game['goals']:
            click.echo(
                f'{goal["goal_minute"]} `{goal["new_score"]}`'
                f' {goal["goalscorer_name"]}')
    else:
        if game["full_time_score"]["home"] > 0 or game[
                "full_time_score"]["away"] > 0:
            click.echo('Goals data is invalid for this game.')
    click.echo()


def get_available_tournaments():
    available_tournaments = []
    for t in get_tournaments.get():
        available_tournaments.append(list(t.items())[1][1])
    return available_tournaments


@click.command()
@click.option(
    '-n', '--number-of-games', default=5, show_default=True, type=int,
    help='Number of last games for the tournament(s).')
@click.option(
    '-t', '--tournament', type=str, multiple=True, default=[],
    help='Tournament name. Possible to pass multiple tournaments.'
         f' Available tournaments: {get_available_tournaments()}')
@click.option(
    '-f', '--time-format', default=False, show_default=True, type=bool,
    help='Use 12 hour format (AM, PM) insted of 24 hour format.')
@click.help_option('-h', '--help')
def main(number_of_games, tournament, time_format):
    """
    Script returns given number of last games
    for the given list of tournaments.

    e.g. cli.py\n
        - to get 5 last games for each available tournament;

    e.g. cli.py -n 10 -t 'Regular Season' -t 'OFB Cup'\n
        - to get 10 last games for each of provided tournaments.
    """
    # TODO option pm/am
    try:
        games = data.main(tournament, number_of_games)
    except Exception as e:
        click.echo(f'Unexpected error: {e}.')
        sys.exit(1)
    for k, v in games.items():
        click.echo(f'{k} last {min(number_of_games, len(v))} games:')
        click.echo()
        for game in v:
            deserialize_game(game, time_format)
        click.echo()


if __name__ == '__main__':
    main()
