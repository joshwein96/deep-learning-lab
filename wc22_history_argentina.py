from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-05',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 5,
        'opponent_goal': 0,
        'rating': ratings['argentina'],
        'opponent_rating': ratings['estonia'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-01',
        'is_play_home': False,
        'is_cup': is_cup['finalissima'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['argentina'],
        'opponent_rating': ratings['italy'],
        'coach': 0,
        'league_id': league_ids['finalissima']
    },
    {
        'match_date': '2022-03-02',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['argentina'],
        'opponent_rating': ratings['ecuador'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2022-03-26',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['argentina'],
        'opponent_rating': ratings['venezuela'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2022-02-02',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['argentina'],
        'opponent_rating': ratings['colombia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2022-01-28',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['argentina'],
        'opponent_rating': ratings['chile'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-11-17',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['argentina'],
        'opponent_rating': ratings['brazil'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-11-13',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['argentina'],
        'opponent_rating': ratings['uruguay'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-10-15',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['argentina'],
        'opponent_rating': ratings['peru'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-10-11',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['argentina'],
        'opponent_rating': ratings['uruguay'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    }
]