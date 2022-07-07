from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['tunisia'],
        'opponent_rating': ratings['japan'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-10',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 0,
        'rating': ratings['tunisia'],
        'opponent_rating': ratings['chile'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-06-05',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup_quali'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['tunisia'],
        'opponent_rating': ratings['botsuana'],
        'coach': 0,
        'league_id': league_ids['africa_cup_quali']
    },
    {
        'match_date': '2022-06-02',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup_quali'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['tunisia'],
        'opponent_rating': ratings['equatorial_guinea'],
        'coach': 0,
        'league_id': league_ids['africa_cup_quali']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_af'],
        'goal': 0,
        'opponent_goal': 0,
        'rating': ratings['tunisia'],
        'opponent_rating': ratings['mali'],
        'coach': 0,
        'league_id': league_ids['wc_quali_af']
    },
    {
        'match_date': '2022-03-25',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_af'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['tunisia'],
        'opponent_rating': ratings['mali'],
        'coach': 0,
        'league_id': league_ids['wc_quali_af']
    },
    {
        'match_date': '2022-01-29',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['tunisia'],
        'opponent_rating': ratings['burkina_faso'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-23',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['tunisia'],
        'opponent_rating': ratings['nigeria'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-20',
        'is_play_home': False,
        'is_cup': is_cup['africa_cup'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['tunisia'],
        'opponent_rating': ratings['gambia'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    },
    {
        'match_date': '2022-01-16',
        'is_play_home': True,
        'is_cup': is_cup['africa_cup'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['tunisia'],
        'opponent_rating': ratings['mauritania'],
        'coach': 0,
        'league_id': league_ids['africa_cup']
    }
]