
#
# def test_custom(monkeypatch):
#     metadata = [{'doc': [{'data': {'matches': {'_': '_', '__': '__'}}}]}]
#     monkeypatch.setattr(get_games.get_tournaments, 'get', lambda *_: tournaments)
#     monkeypatch.setattr(
#         main, 'get_last_games_for_all_tournaments', lambda *_: 'games')
#     games = main.main(['bl'], 5)
#     assert games == 'games'
