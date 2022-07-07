from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['belgium'],
        'opponent_rating': ratings['poland'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-11',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['belgium'],
        'opponent_rating': ratings['wales'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-08',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 6,
        'opponent_goal': 1,
        'rating': ratings['belgium'],
        'opponent_rating': ratings['poland'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-03',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 4,
        'rating': ratings['belgium'],
        'opponent_rating': ratings['netherlands'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['belgium'],
        'opponent_rating': ratings['burkina_faso'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-26',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 2,
        'rating': ratings['belgium'],
        'opponent_rating': ratings['ireland'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-16',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['belgium'],
        'opponent_rating': ratings['wales'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-13',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 3,
        'opponent_goal': 1,
        'rating': ratings['belgium'],
        'opponent_rating': ratings['estonia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-09-08',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['belgium'],
        'opponent_rating': ratings['belarus'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-09-05',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['belgium'],
        'opponent_rating': ratings['czech_republic'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]