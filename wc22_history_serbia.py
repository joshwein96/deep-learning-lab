from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-12',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 2,
        'rating': ratings['serbia'],
        'opponent_rating': ratings['slovenia'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-09',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['serbia'],
        'opponent_rating': ratings['sweden'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-05',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['serbia'],
        'opponent_rating': ratings['slovenia'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-02',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['serbia'],
        'opponent_rating': ratings['norway'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 3,
        'rating': ratings['serbia'],
        'opponent_rating': ratings['denmark'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-24',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['serbia'],
        'opponent_rating': ratings['hungary'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-14',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['serbia'],
        'opponent_rating': ratings['portugal'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-12',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 3,
        'opponent_goal': 1,
        'rating': ratings['serbia'],
        'opponent_rating': ratings['azerbaijan'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-09',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['serbia'],
        'opponent_rating': ratings['luxembourg'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-09-07',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['serbia'],
        'opponent_rating': ratings['ireland'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]