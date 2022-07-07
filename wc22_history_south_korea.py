from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['south_korea'],
        'opponent_rating': ratings['egypt'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-10',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 2,
        'rating': ratings['south_korea'],
        'opponent_rating': ratings['paraguay'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-06',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['south_korea'],
        'opponent_rating': ratings['chile'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-02',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 5,
        'rating': ratings['south_korea'],
        'opponent_rating': ratings['brazil'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['south_korea'],
        'opponent_rating': ratings['uae'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-03-24',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['south_korea'],
        'opponent_rating': ratings['iran'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-02-01',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['south_korea'],
        'opponent_rating': ratings['syria'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-01-27',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['south_korea'],
        'opponent_rating': ratings['libanon'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-01-21',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['south_korea'],
        'opponent_rating': ratings['moldavia'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-01-15',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 5,
        'opponent_goal': 1,
        'rating': ratings['south_korea'],
        'opponent_rating': ratings['iceland'],
        'coach': 0,
        'league_id': league_ids['friendly']
    }
]
