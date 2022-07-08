from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-12',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['spain'],
        'opponent_rating': ratings['czech_republic'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-09',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['spain'],
        'opponent_rating': ratings['switzerland'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-05',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 2,
        'rating': ratings['spain'],
        'opponent_rating': ratings['czech_republic'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-02',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['spain'],
        'opponent_rating': ratings['portugal'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 5,
        'opponent_goal': 0,
        'rating': ratings['spain'],
        'opponent_rating': ratings['iceland'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-26',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['spain'],
        'opponent_rating': ratings['albania'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-14',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['spain'],
        'opponent_rating': ratings['sweden'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-11',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['spain'],
        'opponent_rating': ratings['greece'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-09-08',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['spain'],
        'opponent_rating': ratings['kosovo'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-09-05',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['spain'],
        'opponent_rating': ratings['georgia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]