from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-12',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['switzerland'],
        'opponent_rating': ratings['italy'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-09',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['switzerland'],
        'opponent_rating': ratings['spain'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-05',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 4,
        'rating': ratings['switzerland'],
        'opponent_rating': ratings['portugal'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-02',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['switzerland'],
        'opponent_rating': ratings['czech_republic'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['switzerland'],
        'opponent_rating': ratings['kosovo'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-26',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['switzerland'],
        'opponent_rating': ratings['england'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-15',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['switzerland'],
        'opponent_rating': ratings['bulgaria'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-12',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['switzerland'],
        'opponent_rating': ratings['italy'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-12',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['switzerland'],
        'opponent_rating': ratings['lithuania'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-09',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['switzerland'],
        'opponent_rating': ratings['northern_ireland'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]