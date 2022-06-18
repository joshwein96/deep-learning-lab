import wandb
import numpy as np
import pandas as pd

import xgboost as xgb
import multiprocessing
import pandas as pd
import matplotlib.pyplot as plt

#imports for train function
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import xgboost as xgb
from ray import tune
from ray.tune.integration.xgboost import TuneReportCheckpointCallback


df = pd.read_csv(r"/home/up087847/DLLab/train.csv", low_memory=False)
columns = list(df.columns)

f_target, f_home_team_name, f_away_team_name, f_match_date = [[feature] for feature in columns[1:5]]
f_league_name, f_league_id, f_is_cup, f_home_team_coach_id, f_away_team_coach_id = [[feature] for feature in columns[5:10]]

f_home_team_history_match_date = columns[10:20]
f_home_team_history_is_play_home = columns[20:30]
f_home_team_history_is_cup = columns[30:40]
f_home_team_history_goal = columns[40:50]
f_home_team_history_opponent_goal = columns[50:60]
f_home_team_history_rating = columns[60:70]
f_home_team_history_opponent_rating = columns[70:80]
f_home_team_history_coach = columns[80:90]
f_home_team_history_league_id = columns[90:100]
f_away_team_history_match_date = columns[100:110]
f_away_team_history_is_play_home = columns[110:120]
f_away_team_history_is_cup = columns[120:130]
f_away_team_history_goal = columns[130:140]
f_away_team_history_opponent_goal = columns[140:150]
f_away_team_history_rating = columns[150:160]
f_away_team_history_opponent_rating = columns[160:170]
f_away_team_history_coach = columns[170:180]
f_away_team_history_league_id = columns[180:190]

features_shitty = f_match_date + f_home_team_coach_id + f_away_team_coach_id + f_home_team_history_match_date + f_home_team_history_coach + f_away_team_history_match_date + f_away_team_history_coach
features_boolean = f_is_cup + f_home_team_history_is_play_home + f_home_team_history_is_cup + f_away_team_history_is_play_home + f_away_team_history_is_cup
features_numerical = f_home_team_history_goal + f_home_team_history_opponent_goal + f_home_team_history_rating + f_home_team_history_opponent_rating + f_away_team_history_goal + f_away_team_history_opponent_goal + f_away_team_history_rating + f_away_team_history_opponent_rating
features_categorical = f_home_team_name + f_away_team_name + f_league_name + f_league_id + f_home_team_history_league_id + f_away_team_history_league_id

# drop NaN and duplicates
df = df.dropna()
df = df.drop_duplicates()

# data processing 
data_set = df[['id']]
data_set = data_set.join((df['target']))
data_set = data_set.join(df[features_boolean].astype(int))
data_set = data_set.join(df[features_numerical].astype(float))

y = data_set.columns[1]
x = data_set.columns[2:]
#target
Y=data_set[y]
#train
X=data_set[x]

#label encoding
label_encoder = LabelEncoder()
label_encoder = label_encoder.fit(Y)
label_encoded_y = label_encoder.transform(Y)


X_train, X_valid, y_train, y_valid = train_test_split(X, label_encoded_y, train_size=0.8, random_state=42)

#d_train = xgb.DMatrix(X_train, y_train)
#d_test = xgb.DMatrix(X_valid, y_valid)

def train_prediction(config: dict):
    d_train = xgb.DMatrix(X_train, y_train)
    d_test = xgb.DMatrix(X_valid, y_valid)
    results = {}
    num_round=10
    xgb.train(
         config,
         d_train,
         num_round,
         evals=[(d_test, "eval")],
         evals_result=results,
         verbose_eval=False)
    mlogloss=results['eval']['mlogloss'][-1]
    tune.report(mlogloss=mlogloss, done=True)

config = {
    'booster': 'gbtree',
    'max_depth': tune.randint(1, 8),
    'learning_rate': tune.loguniform(1e-4, 4e-1),
    'min_split_loss': 0.01,
    'min_child_weight': tune.choice([1, 2, 3]),
    'subsample': tune.uniform(0.5, 1.0),
    'colsample_bytree': 1,
    'objective': 'multi:softprob',
    'num_class': 3,
    'eval_metric':'mlogloss'
    }
#num_round = 10
#evallist = [(d_train, 'train'), (d_test, 'eval')]
#results={}
#bst = xgb.train(config, d_train, num_round, evallist, evals_result=results, early_stopping_rounds=10)

analysis = tune.run(
    train_prediction,
    metric="mlogloss",
    mode="min",
    resources_per_trial={"cpu": 1},
    config=config,
    num_samples=3,
    verbose=3)

print(f"Best model parameters: {analysis.best_config}")
print(f" Best achieved loss: {analysis.best_result['mlogloss']}")