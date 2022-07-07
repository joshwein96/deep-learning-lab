from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': True,
        'is_cup': is_cup['wc_playoffs'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['new_zeeland'],
        'coach': 0,
        'league_id': league_ids['wc_playoffs']
    },
    {
        'match_date': '2022-06-05',
        'is_play_home': True,
        'is_cup': is_cup['nations_concacaf'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['martinique'],
        'coach': 0,
        'league_id': league_ids['nations_concacaf']
    },
    {
        'match_date': '2022-06-03',
        'is_play_home': False,
        'is_cup': is_cup['nations_concacaf'],
        'goal': 0,
        'opponent_goal': 2,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['panama'],
        'coach': 0,
        'league_id': league_ids['nations_concacaf']
    },
    {
        'match_date': '2022-03-31',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['usa'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-03-27',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['el_salvador'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-02-03',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['jamaica'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-02-03',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['mexico'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2022-01-28',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['panama'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2021-11-17',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['honduras'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2021-11-13',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['canada'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    },
    {
        'match_date': '2021-10-14',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_na'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['costa_rica'],
        'opponent_rating': ratings['usa'],
        'coach': 0,
        'league_id': league_ids['wc_quali_na']
    }
]