from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 3,
        'opponent_goal': 1,
        'rating': ratings['ghana'],
        'opponent_rating': ratings['chile'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-10',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 4,
        'rating': ratings['ghana'],
        'opponent_rating': ratings['japan'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-05',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup_quali'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['ghana'],
        'opponent_rating': ratings['central_africa'],
        'coach': 0,
        'league_id': league_ids['africa_cup_quali']
    },
    {
        'match_date': '2022-06-01',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup_quali'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['ghana'],
        'opponent_rating': ratings['madagascar'],
        'coach': 0,
        'league_id': league_ids['africa_cup_quali']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_af'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['ghana'],
        'opponent_rating': ratings['nigeria'],
        'coach': 0,
        'league_id': league_ids['wc_quali_af']
    },
    {
        'match_date': '2022-02-25',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_af'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['ghana'],
        'opponent_rating': ratings['nigeria'],
        'coach': 0,
        'league_id': league_ids['wc_quali_af']
    },
    {
        'match_date': '2022-01-18',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 2,
        'opponent_goal': 3,
        'rating': ratings['ghana'],
        'opponent_rating': ratings['comoros'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-14',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['ghana'],
        'opponent_rating': ratings['gabon'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-10',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['ghana'],
        'opponent_rating': ratings['morocco'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-05',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 3,
        'rating': ratings['ghana'],
        'opponent_rating': ratings['algeria'],
        'coach': 0,
        'league_id': league_ids['friendly']
    }
]