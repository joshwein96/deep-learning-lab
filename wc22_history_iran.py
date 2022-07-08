from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-0612',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['iran'],
        'opponent_rating': ratings['algeria'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['iran'],
        'opponent_rating': ratings['libanon'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-03-24',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 0,
        'opponent_goal': 2,
        'rating': ratings['iran'],
        'opponent_rating': ratings['south_korea'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-02-01',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['iran'],
        'opponent_rating': ratings['uae'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-01-27',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['iran'],
        'opponent_rating': ratings['iraq'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-11-16',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['iran'],
        'opponent_rating': ratings['syria'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-11-11',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['iran'],
        'opponent_rating': ratings['libanon'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-10-12',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['iran'],
        'opponent_rating': ratings['south_korea'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-10-07',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['iran'],
        'opponent_rating': ratings['uae'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-09-07',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['iran'],
        'opponent_rating': ratings['iraq'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    }
]