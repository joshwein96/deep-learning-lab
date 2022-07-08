from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-06',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['brazil'],
        'opponent_rating': ratings['japan'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-02',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 5,
        'opponent_goal': 1,
        'rating': ratings['brazil'],
        'opponent_rating': ratings['south_korea'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-30',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['brazil'],
        'opponent_rating': ratings['bolivia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2022-03-25',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['brazil'],
        'opponent_rating': ratings['chile'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2022-02-02',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['brazil'],
        'opponent_rating': ratings['paraguay'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2022-01-27',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['brazil'],
        'opponent_rating': ratings['ecuador'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-11-17',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['brazil'],
        'opponent_rating': ratings['argentina'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-11-12',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['brazil'],
        'opponent_rating': ratings['colombia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-10-15',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['brazil'],
        'opponent_rating': ratings['uruguay'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-10-10',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['brazil'],
        'opponent_rating': ratings['colombia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    }
]