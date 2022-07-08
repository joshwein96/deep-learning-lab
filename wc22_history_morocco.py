from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-13',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup_quali'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['morocco'],
        'opponent_rating': ratings['liberia'],
        'coach': 0,
        'league_id': league_ids['africa_cup_quali']
    },
    {
        'match_date': '2022-06-09',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup_quali'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['morocco'],
        'opponent_rating': ratings['south_africa'],
        'coach': 0,
        'league_id': league_ids['africa_cup_quali']
    },
    {
        'match_date': '2022-06-02',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 0,
        'opponent_goal': 3,
        'rating': ratings['morocco'],
        'opponent_rating': ratings['usa'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_af'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['morocco'],
        'opponent_rating': ratings['congo'],
        'coach': 0,
        'league_id': league_ids['wc_quali_af']
    },
    {
        'match_date': '2022-03-25',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_af'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['morocco'],
        'opponent_rating': ratings['congo'],
        'coach': 0,
        'league_id': league_ids['wc_quali_af']
    },
    {
        'match_date': '2022-01-30',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['morocco'],
        'opponent_rating': ratings['egypt'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-25',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['morocco'],
        'opponent_rating': ratings['malawi'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-18',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 2,
        'opponent_goal': 2,
        'rating': ratings['morocco'],
        'opponent_rating': ratings['gabon'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-14',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['morocco'],
        'opponent_rating': ratings['comoros'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-10',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['morocco'],
        'opponent_rating': ratings['ghana'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    }
]