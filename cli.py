#!/usr/bin/env python
import click

import main


@click.command()
@click.option(
    '-n', '--number-of-games', default=5, show_default=True, type=int,
    help='Number of last games for the tournament(s).')
@click.option(
    '-t', '--tournament', type=str, multiple=True, default=[],
    help='Tournament name. Possible to pass multiple tournaments.')
@click.help_option('-h', '--help')
def main(number_of_games, tournament):
    """
    Script returns given number of last games
    for the given list of tournaments.

    e.g. cli.py -n 10 -t 'Regular Season' -t
    """
    main.data(list(tournament), number_of_games)


if __name__ == '__main__':
    main()
