from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-13',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['france'],
        'opponent_rating': ratings['croatia'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-10',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['france'],
        'opponent_rating': ratings['austria'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-06',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['france'],
        'opponent_rating': ratings['croatia'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-03',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['france'],
        'opponent_rating': ratings['denmark'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 5,
        'opponent_goal': 0,
        'rating': ratings['france'],
        'opponent_rating': ratings['south_africa'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-25',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['france'],
        'opponent_rating': ratings['ivory_coast'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-16',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['france'],
        'opponent_rating': ratings['finland'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-13',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 8,
        'opponent_goal': 0,
        'rating': ratings['france'],
        'opponent_rating': ratings['kazakhstan'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-09-07',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['france'],
        'opponent_rating': ratings['finland'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-09-04',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['france'],
        'opponent_rating': ratings['ukraine'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]