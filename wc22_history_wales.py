from wc22_data import is_cup, league_ids, ratings

games = [
    {
        'match_date': '2022-06-14',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 2,
        'opponent_goal': 3,
        'rating': ratings['wales'],
        'opponent_rating': ratings['netherlands'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-11',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['wales'],
        'opponent_rating': ratings['belgium'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-08',
        'is_play_home': True,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['wales'],
        'opponent_rating': ratings['netherlands'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-06-05',
        'is_play_home': True,
        'is_cup': is_cup['wc_playoffs'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['wales'],
        'opponent_rating': ratings['ukraine'],
        'coach': 0,
        'league_id': league_ids['wc_playoffs']
    },
    {
        'match_date': '2022-06-01',
        'is_play_home': False,
        'is_cup': is_cup['nations_uefa'],
        'goal': 1,
        'opponent_goal': 2,
        'rating': ratings['wales'],
        'opponent_rating': ratings['poland'],
        'coach': 0,
        'league_id': league_ids['nations_uefa']
    },
    {
        'match_date': '2022-03-29',
        'is_play_home': True,
        'is_cup': is_cup['friendly'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['wales'],
        'opponent_rating': ratings['czech_republic'],
        'coach': 0,
        'league_id': league_ids['friendly']
    },
    {
        'match_date': '2022-03-24',
        'is_play_home': True,
        'is_cup': is_cup['wc_playoffs'],
        'goal': 2,
        'opponent_goal': 1,
        'rating': ratings['wales'],
        'opponent_rating': ratings['austria'],
        'coach': 0,
        'league_id': league_ids['wc_playoffs']
    },
    {
        'match_date': '2021-11-16',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 1,
        'rating': ratings['wales'],
        'opponent_rating': ratings['belgium'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2021-11-13',
        'is_play_home': True,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 5,
        'opponent_goal': 1,
        'rating': ratings['wales'],
        'opponent_rating': ratings['belarus'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    },
    {
        'match_date': '2022-11-11',
        'is_play_home': False,
        'is_cup': is_cup['wc_quali_eu'],
        'goal': 1,
        'opponent_goal': 0,
        'rating': ratings['wales'],
        'opponent_rating': ratings['estonia'],
        'coach': 0,
        'league_id': league_ids['wc_quali_eu']
    }
]