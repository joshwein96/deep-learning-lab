from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 3,
        'rating': ratings['japan'],
        'opponent_rating': ratings['tunisia'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-10',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['japan'],
        'opponent_rating': ratings['ghana'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-06',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['japan'],
        'opponent_rating': ratings['brazil'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-02',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['japan'],
        'opponent_rating': ratings['paraguay'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['japan'],
        'opponent_rating': ratings['vietnam'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-03-24',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['japan'],
        'opponent_rating': ratings['australia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-02-01',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['japan'],
        'opponent_rating': ratings['saudi_arabia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2022-01-27',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_as'],
        'goal':2 ,
        'opponent_goal': 0,
        'rating': ratings['japan'],
        'opponent_rating': ratings['china'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-11-16',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['japan'],
        'opponent_rating': ratings['oman'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    },
    {
        'match_date': '2021-11-11',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_as'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['japan'],
        'opponent_rating': ratings['vietnam'],
        'coach': 0,
        'league_id': league_ids['wc_quali_as']
    }
]