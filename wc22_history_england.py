from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 4,
        'rating': ratings['england'],
        'opponent_rating': ratings['hungary'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-11',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['england'],
        'opponent_rating': ratings['italy'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-07',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['england'],
        'opponent_rating': ratings['germany'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-04',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['england'],
        'opponent_rating': ratings['hungary'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['england'],
        'opponent_rating': ratings['ivory_coast'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-26',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['england'],
        'opponent_rating': ratings['switzerland'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-15',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 10,
        'opponent_goal': 0,
        'rating': ratings['england'],
        'opponent_rating': ratings['san_marino'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-12',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 5,
        'opponent_goal': 0,
        'rating': ratings['england'],
        'opponent_rating': ratings['albania'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2022-10-12',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['england'],
        'opponent_rating': ratings['hungary'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2022-10-09',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 5,
        'opponent_goal': 0,
        'rating': ratings['england'],
        'opponent_rating': ratings['andorra'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]