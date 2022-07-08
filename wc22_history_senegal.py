from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-07',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup_quali'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['senegal'],
        'opponent_rating': ratings['rwanda'],
        'coach': 0,
        'league_id': league_ids['africa_cup_quali']
    },
    {
        'match_date': '2022-06-04',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup_quali'],
        'goal': 3,
        'opponent_goal': 1,
        'rating': ratings['senegal'],
        'opponent_rating': ratings['benin'],
        'coach': 0,
        'league_id': league_ids['africa_cup_quali']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_af'],
        'goal': 3,
        'opponent_goal': 1,
        'rating': ratings['senegal'],
        'opponent_rating': ratings['egypt'],
        'coach': 0,
        'league_id': league_ids['wc_quali_af']
    },
    {
        'match_date': '2022-03-25',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_af'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['senegal'],
        'opponent_rating': ratings['egypt'],
        'coach': 0,
        'league_id': league_ids['wc_quali_af']
    },
    {
        'match_date': '2022-02-06',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 4,
        'opponent_goal': 2,
        'rating': ratings['senegal'],
        'opponent_rating': ratings['egypt'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-02-02',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 3,
        'opponent_goal': 1,
        'rating': ratings['senegal'],
        'opponent_rating': ratings['burkina_faso'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-30',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 3,
        'opponent_goal': 1,
        'rating': ratings['senegal'],
        'opponent_rating': ratings['equatorial_guinea'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-25',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['senegal'],
        'opponent_rating': ratings['cape_verde'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-18',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['senegal'],
        'opponent_rating': ratings['malawi'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-14',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['senegal'],
        'opponent_rating': ratings['guinea'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    }
]