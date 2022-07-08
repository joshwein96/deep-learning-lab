from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['qatar'],
        'opponent_rating': ratings['slovenia'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-26',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['qatar'],
        'opponent_rating': ratings['bulgaria'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-12-18',
        'is_play_home': False,
        'is_cup': is_cup['arab_cup'],
        'goal': 5,
        'opponent_goal': 4,
        'rating': ratings['qatar'],
        'opponent_rating': ratings['egypt'],
        'coach': 0,
        'league_id': league_ids['arab_cup']
    },
    {
        'match_date': '2021-12-15',
        'is_play_home': True,
        'is_cup': is_cup['arab_cup'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['qatar'],
        'opponent_rating': ratings['algeria'],
        'coach': 0,
        'league_id': league_ids['arab_cup']
    },
    {
        'match_date': '2021-12-10',
        'is_play_home': True,
        'is_cup': is_cup['arab_cup'],
        'goal': 5,
        'opponent_goal': 0,
        'rating': ratings['qatar'],
        'opponent_rating': ratings['uae'],
        'coach': 0,
        'league_id': league_ids['arab_cup']
    },
    {
        'match_date': '2021-12-06',
        'is_play_home': True,
        'is_cup': is_cup['arab_cup'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['qatar'],
        'opponent_rating': ratings['iraq'],
        'coach': 0,
        'league_id': league_ids['arab_cup']
    },
    {
        'match_date': '2021-12-03',
        'is_play_home': False,
        'is_cup': is_cup['arab_cup'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['qatar'],
        'opponent_rating': ratings['oman'],
        'coach': 0,
        'league_id': league_ids['arab_cup']
    },
    {
        'match_date': '2021-11-30',
        'is_play_home': True,
        'is_cup': is_cup['arab_cup'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['qatar'],
        'opponent_rating': ratings['bahrain'],
        'coach': 0,
        'league_id': league_ids['arab_cup']
    },
    {
        'match_date': '2021-07-30',
        'is_play_home': True,
        'is_cup': is_cup['gold_cup'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['qatar'],
        'opponent_rating': ratings['usa'],
        'coach': 0,
        'league_id': league_ids['gold_cup']
    },
    {
        'match_date': '2021-07-25',
        'is_play_home': True,
        'is_cup': is_cup['gold_cup'],
        'goal': 3,
        'opponent_goal': 2,
        'rating': ratings['qatar'],
        'opponent_rating': ratings['el_salvador'],
        'coach': 0,
        'league_id': league_ids['gold_cup']
    }
]