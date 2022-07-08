from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 3,
        'opponent_goal': 2,
        'rating': ratings['netherlands'],
        'opponent_rating': ratings['wales'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-11',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 2,
        'rating': ratings['netherlands'],
        'opponent_rating': ratings['poland'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-08',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['netherlands'],
        'opponent_rating': ratings['wales'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-03',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['netherlands'],
        'opponent_rating': ratings['belgium'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['netherlands'],
        'opponent_rating': ratings['germany'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-02-26',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 4,
        'opponent_goal': 2,
        'rating': ratings['netherlands'],
        'opponent_rating': ratings['denmark'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-16',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['netherlands'],
        'opponent_rating': ratings['norway'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-13',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 2,
        'opponent_goal': 2,
        'rating': ratings['netherlands'],
        'opponent_rating': ratings['montenegro'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-11',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 6,
        'opponent_goal': 0,
        'rating': ratings['netherlands'],
        'opponent_rating': ratings['gibraltar'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-08',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['netherlands'],
        'opponent_rating': ratings['latvia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]