from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-15',
        'is_play_home': False,
        'is_cup': is_cup['nations_concacaf'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['usa'],
        'opponent_rating': ratings['el_salvador'],
        'coach': 0,
        'league_id': league_ids['nations_concacaf']
    },
    {
        'match_date': '2022-06-11',
        'is_play_home': True,
        'is_cup': is_cup['nations_concacaf'],
        'goal': 5,
        'opponent_goal': 0,
        'rating': ratings['usa'],
        'opponent_rating': ratings['grenada'],
        'coach': 0,
        'league_id': league_ids['nations_concacaf']
    },
    {
        'match_date': '2022-06-05',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['usa'],
        'opponent_rating': ratings['uruguay'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-02',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['usa'],
        'opponent_rating': ratings['morocco'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-31',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 0,
        'opponent_goal': 2,
        'rating': ratings['usa'],
        'opponent_rating': ratings['costa_rica'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-03-28',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 5,
        'opponent_goal': 1,
        'rating': ratings['usa'],
        'opponent_rating': ratings['panama'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-03-25',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['usa'],
        'opponent_rating': ratings['mexico'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-02-03',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['usa'],
        'opponent_rating': ratings['honduras'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-01-30',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 0,
        'opponent_goal': 2,
        'rating': ratings['usa'],
        'opponent_rating': ratings['canada'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-01-28',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['usa'],
        'opponent_rating': ratings['el_salvador'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    }
]