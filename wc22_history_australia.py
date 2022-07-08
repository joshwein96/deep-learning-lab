from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-13',
        'is_play_home': True,
        'is_cup': is_cup['wc_playoffs'],
        'goal': 5,
        'opponent_goal': 4,
        'rating': ratings['australia'],
        'opponent_rating': ratings['peru'],
        'coach': 0,
        'league_id': league_ids['wc_playoffs']
    },
    {
        'match_date': '2022-06-07',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['australia'],
        'opponent_rating': ratings['uae'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-06-01',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['australia'],
        'opponent_rating': ratings['jordan'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['australia'],
        'opponent_rating': ratings['saudi_arabia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-03-24',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 0,
        'opponent_goal': 2,
        'rating': ratings['australia'],
        'opponent_rating': ratings['japan'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-02-01',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 2,
        'opponent_goal': 2,
        'rating': ratings['australia'],
        'opponent_rating': ratings['oman'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-01-27',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['australia'],
        'opponent_rating': ratings['vietnam'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-11-16',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['australia'],
        'opponent_rating': ratings['china'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-11-11',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['australia'],
        'opponent_rating': ratings['saudi_arabia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-10-12',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['australia'],
        'opponent_rating': ratings['japan'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    }
]