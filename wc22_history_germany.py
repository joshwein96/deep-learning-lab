from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 5,
        'opponent_goal': 2,
        'rating': ratings['germany'],
        'opponent_rating': ratings['italy'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-11',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['germany'],
        'opponent_rating': ratings['hungary'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-07',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['germany'],
        'opponent_rating': ratings['england'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-04',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['germany'],
        'opponent_rating': ratings['italy'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['germany'],
        'opponent_rating': ratings['netherlands'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-26',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['germany'],
        'opponent_rating': ratings['israel'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-14',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['germany'],
        'opponent_rating': ratings['armenia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-11',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 9,
        'opponent_goal': 0,
        'rating': ratings['germany'],
        'opponent_rating': ratings['liechtenstein'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-11',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['germany'],
        'opponent_rating': ratings['north_macedonia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-08',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['germany'],
        'opponent_rating': ratings['romania'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]