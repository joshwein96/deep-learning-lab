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


preprocessed=pd.read_csv('preprocessed.csv')
y = preprocessed.columns[1]
x = preprocessed.columns[2:]

Y=preprocessed[y]
X=preprocessed[x]


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
    num_round=100
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
    num_samples=4,
    verbose=3,
    resume=None)

print(f"Best model parameters: {analysis.best_config}")
print(f" Best achieved loss: {analysis.best_result['mlogloss']}")