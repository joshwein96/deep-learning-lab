from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-13',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal':2 ,
        'opponent_goal': 0,
        'rating': ratings['denmark'],
        'opponent_rating': ratings['austria'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-10',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 0,
        'opponent_goal': 1,
        'rating': ratings['denmark'],
        'opponent_rating': ratings['croatia'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-06',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['denmark'],
        'opponent_rating': ratings['austria'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-03',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['denmark'],
        'opponent_rating': ratings['france'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 3,
        'opponent_goal': 0,
        'rating': ratings['denmark'],
        'opponent_rating': ratings['serbia'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-26',
        'is_play_home': False,
        'is_cup': is_cup['friendly'],
        'goal': 2,
        'opponent_goal': 4,
        'rating': ratings['denmark'],
        'opponent_rating': ratings['netherlands'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2021-11-15',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 0,
        'opponent_goal': 2,
        'rating': ratings['denmark'],
        'opponent_rating': ratings['scotland'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-12',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 3,
        'opponent_goal': 1,
        'rating': ratings['denmark'],
        'opponent_rating': ratings['faroe_islands'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-12',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['denmark'],
        'opponent_rating': ratings['austria'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-10-09',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 4,
        'opponent_goal': 0,
        'rating': ratings['denmark'],
        'opponent_rating': ratings['moldavia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]