from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-05',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['uruguay'],
        'opponent_rating': ratings['usa'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-03',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['uruguay'],
        'opponent_rating': ratings['mexico'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-30',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['uruguay'],
        'opponent_rating': ratings['chile'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2022-03-25',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['uruguay'],
        'opponent_rating': ratings['peru'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2022-02-02',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['uruguay'],
        'opponent_rating': ratings['venezuela'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2022-01-28',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['uruguay'],
        'opponent_rating': ratings['paraguay'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-11-16',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 0,
        'opponent_goal': 3,
        'rating': ratings['uruguay'],
        'opponent_rating': ratings['bolivia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-11-13',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['uruguay'],
        'opponent_rating': ratings['argentina'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-10-15',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 1,
        'opponent_goal': 4,
        'rating': ratings['uruguay'],
        'opponent_rating': ratings['brazil'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    },
    {
        'match_date': '2021-10-11',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_sa'],
        'goal': 0,
        'opponent_goal': 3,
        'rating': ratings['uruguay'],
        'opponent_rating': ratings['argentina'],
        'coach': 0,
        'league_id': league_ids['wc_quali_sa']
    }
]