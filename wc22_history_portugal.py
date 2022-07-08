from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-12',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['portugal'],
        'opponent_rating': ratings['switzerland'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-09',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['portugal'],
        'opponent_rating': ratings['czech_republic'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-05',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['portugal'],
        'opponent_rating': ratings['switzerland'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-02',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['portugal'],
        'opponent_rating': ratings['spain'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['portugal'],
        'opponent_rating': ratings['north_macedonia'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-24',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 3,
        'opponent_goal': 1,
        'rating': ratings['portugal'],
        'opponent_rating': ratings['turkey'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-14',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['portugal'],
        'opponent_rating': ratings['serbia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-11',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['portugal'],
        'opponent_rating': ratings['ireland'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-12',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 5,
        'opponent_goal': 0,
        'rating': ratings['portugal'],
        'opponent_rating': ratings['luxembourg'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-09-07',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['portugal'],
        'opponent_rating': ratings['azerbaijan'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]