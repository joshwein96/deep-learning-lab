from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-09',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['saudi_arabia'],
        'opponent_rating': ratings['venezuela'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-05',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['saudi_arabia'],
        'opponent_rating': ratings['colombia'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['saudi_arabia'],
        'opponent_rating': ratings['australia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-03-24',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['saudi_arabia'],
        'opponent_rating': ratings['china'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-02-01',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 0,
        'opponent_goal': 2,
        'rating': ratings['saudi_arabia'],
        'opponent_rating': ratings['japan'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-01-27',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['saudi_arabia'],
        'opponent_rating': ratings['oman'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-12-07',
        'is_play_home': False,
        'is_cup': is_cup['arab_cup'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['saudi_arabia'],
        'opponent_rating': ratings['morocco'],
        'coach': 0,
        'league_id': league_ids['arab_cup']
    },
    {
        'match_date': '2021-12-04',
        'is_play_home': False,
        'is_cup': is_cup['arab_cup'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['saudi_arabia'],
        'opponent_rating': ratings['palestine'],
        'coach': 0,
        'league_id': league_ids['arab_cup']
    },
    {
        'match_date': '2021-12-01',
        'is_play_home': True,
        'is_cup': is_cup['arab_cup'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['saudi_arabia'],
        'opponent_rating': ratings['jordan'],
        'coach': 0,
        'league_id': league_ids['arab_cup']
    },
    {
        'match_date': '2021-11-16',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['saudi_arabia'],
        'opponent_rating': ratings['vietnam'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    }
]