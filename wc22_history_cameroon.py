from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-09',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup_quali'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['cameroon'],
        'opponent_rating': ratings['burundi'],
        'coach': 0,
        'league_id': league_ids['africa_cup_quali']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_af'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['cameroon'],
        'opponent_rating': ratings['algeria'],
        'coach': 0,
        'league_id': league_ids['wc_quali_af']
    },
    {
        'match_date': '2022-03-25',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_af'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['cameroon'],
        'opponent_rating': ratings['algeria'],
        'coach': 0,
        'league_id': league_ids['wc_quali_af']
    },
    {
        'match_date': '2022-02-05',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 5,
        'opponent_goal': 3,
        'rating': ratings['cameroon'],
        'opponent_rating': ratings['burkina_faso'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-02-03',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 1,
        'opponent_goal': 3,
        'rating': ratings['cameroon'],
        'opponent_rating': ratings['egypt'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-29',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['cameroon'],
        'opponent_rating': ratings['gambia'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-24',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['cameroon'],
        'opponent_rating': ratings['comoros'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-17',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['cameroon'],
        'opponent_rating': ratings['cape_verde'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-13',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 4,
        'opponent_goal': 1,
        'rating': ratings['cameroon'],
        'opponent_rating': ratings['ethiopia'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-09',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['cameroon'],
        'opponent_rating': ratings['burkina_faso'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    }
]