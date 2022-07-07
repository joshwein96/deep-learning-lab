from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-15',
        'is_play_home': False,
        'is_cup': is_cup['nations_concacaf'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['mexico'],
        'opponent_rating': ratings['jamaica'],
        'coach': 0,
        'league_id': league_ids['nations_concacaf']
    },
    {
        'match_date': '2022-06-12',
        'is_play_home': True,
        'is_cup': is_cup['nations_concacaf'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['mexico'],
        'opponent_rating': ratings['surinam'],
        'coach': 0,
        'league_id': league_ids['nations_concacaf']
    },
    {
        'match_date': '2022-06-06',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['mexico'],
        'opponent_rating': ratings['ecuador'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-03',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 3,
        'rating': ratings['mexico'],
        'opponent_rating': ratings['uruguay'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-05-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['mexico'],
        'opponent_rating': ratings['nigeria'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-04-28',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['mexico'],
        'opponent_rating': ratings['guatemala'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-31',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['mexico'],
        'opponent_rating': ratings['el_salvador'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-03-28',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['mexico'],
        'opponent_rating': ratings['honduras'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-03-25',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['mexico'],
        'opponent_rating': ratings['usa'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-02-03',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['mexico'],
        'opponent_rating': ratings['panama'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    }
]