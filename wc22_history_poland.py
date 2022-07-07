from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['poland'],
        'opponent_rating': ratings['belgium'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-11',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 2,
        'rating': ratings['poland'],
        'opponent_rating': ratings['netherlands'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-08',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 6,
        'rating': ratings['poland'],
        'opponent_rating': ratings['belgium'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-01',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['poland'],
        'opponent_rating': ratings['wales'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['wc_playoffs'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['poland'],
        'opponent_rating': ratings['sweden'],
        'coach': 0,
        'league_id': league_ids['wc_playoffs']
    },
    {
        'match_date': '2022-03-24',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['poland'],
        'opponent_rating': ratings['scotland'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-15',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['poland'],
        'opponent_rating': ratings['hungary'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-12',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['poland'],
        'opponent_rating': ratings['andorra'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-12',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['poland'],
        'opponent_rating': ratings['albania'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2022-10-09',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 5,
        'opponent_goal': 0,
        'rating': ratings['poland'],
        'opponent_rating': ratings['san_marino'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
]