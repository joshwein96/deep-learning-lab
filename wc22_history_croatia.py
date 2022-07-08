from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-13',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['croatia'],
        'opponent_rating': ratings['france'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-10',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['croatia'],
        'opponent_rating': ratings['denmark'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-06',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['croatia'],
        'opponent_rating': ratings['france'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-03',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 3,
        'rating': ratings['croatia'],
        'opponent_rating': ratings['austria'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['croatia'],
        'opponent_rating': ratings['bulgaria'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-26',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['croatia'],
        'opponent_rating': ratings['slovenia'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-14',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['croatia'],
        'opponent_rating': ratings['russia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-11',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 7,
        'opponent_goal': 1,
        'rating': ratings['croatia'],
        'opponent_rating': ratings['malta'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-11',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 2,
        'opponent_goal': 2,
        'rating': ratings['croatia'],
        'opponent_rating': ratings['slovakia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-08',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['croatia'],
        'opponent_rating': ratings['cyprus'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]