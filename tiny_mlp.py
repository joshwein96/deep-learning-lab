import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.backends.cudnn as cudnn

import wandb
import numpy as np
import pandas as pd

from fastprogress import master_bar, progress_bar
from sklearn.model_selection import train_test_split

# login to weights and biases
wandb.login(key='your_api_key')

# read dataset as pandas dataframe
df = pd.read_csv('train.csv', low_memory=False)

# determine features
columns = list(df.columns)

# store feature names in variables
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

# split features in four categories
features_shitty = f_match_date + f_home_team_coach_id + f_away_team_coach_id + f_home_team_history_match_date + f_home_team_history_coach + f_away_team_history_match_date + f_away_team_history_coach
features_boolean = f_is_cup + f_home_team_history_is_play_home + f_home_team_history_is_cup + f_away_team_history_is_play_home + f_away_team_history_is_cup
features_numerical = f_home_team_history_goal + f_home_team_history_opponent_goal + f_home_team_history_rating + f_home_team_history_opponent_rating + f_away_team_history_goal + f_away_team_history_opponent_goal + f_away_team_history_rating + f_away_team_history_opponent_rating
features_categorical = f_home_team_name + f_away_team_name + f_league_name + f_league_id + f_home_team_history_league_id + f_away_team_history_league_id

# drop NaN and duplicates
df = df.dropna()
df = df.drop_duplicates()

# data processing
data_set = df[['id']]
data_set = data_set.join(pd.get_dummies(df['target']))
data_set = data_set.join(df[features_boolean].astype(int))
data_set = data_set.join(df[features_numerical].astype(float))
data_set = data_set.join(pd.get_dummies(df[features_categorical[0:3]]))

# transform data to tensor
targets = data_set.columns[1:4]
features = data_set.columns[4:]
x = torch.tensor(data_set[features].values).float()
y = torch.tensor(data_set[targets].values).float()

# define custom dataset
class DataSet():

    def __init__(self,x,y):
        self.x_train = x
        self.y_train = y

    def __len__(self):
        return len(self.y_train)

    def __getitem__(self,idx):
        return self.x_train[idx], self.y_train[idx]

# split data in train and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=33)

# set up dataloaders
train_loader = torch.utils.data.DataLoader(DataSet(x_train,y_train), batch_size=128, shuffle=True)
test_loader =  torch.utils.data.DataLoader(DataSet(x_test,y_test), batch_size=128, shuffle=True)

# Check GPU access
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Running on {device}')
if device == 'cuda':
    cudnn.benchmark = True
else:
    print('Are you sure you want to run on CPU?')

# define the model
class MLP(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(11033, 8000)
        self.fc2 = nn.Linear(8000, 5000)
        self.fc3 = nn.Linear(5000, 2000)
        self.fc4 = nn.Linear(2000, 500)
        self.fc5 = nn.Linear(500, 3)
        nn.init.kaiming_uniform_(self.fc1.weight, nonlinearity='relu')
        nn.init.kaiming_uniform_(self.fc2.weight, nonlinearity='relu')
        nn.init.kaiming_uniform_(self.fc3.weight, nonlinearity='relu')
        nn.init.kaiming_uniform_(self.fc4.weight, nonlinearity='relu')
        nn.init.xavier_uniform_(self.fc5.weight)
        nn.init.constant_(self.fc1.bias, 0.0)
        nn.init.constant_(self.fc2.bias, 0.0)
        nn.init.constant_(self.fc3.bias, 0.0)
        nn.init.constant_(self.fc4.bias, 0.0)
        nn.init.constant_(self.fc5.bias, 0.0)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = F.softmax(self.fc5(x))
        return x

model = MLP().to(device)
model.float()

# prepare training
learning_rate = 0.005
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

def test_model(model):
    
    train_mode = model.training
    
    if train_mode:
        model.eval()
    
    # set up confusion matrix
    confusion = np.zeros((3,3), dtype=np.int32)
        
    # iterate train set
    for inputs, labels in iter(test_loader):
        inputs = inputs.to(device)
        outputs = model(inputs)
        for label, output in zip(labels, outputs.cpu().detach().numpy()):
            confusion[np.argmax(label), np.argmax(output)] += 1

    # compute some metrics
    total = np.sum(confusion)
    accuracy = np.sum(np.diag(confusion)) / total
    per_class_accuracy = np.diag(confusion) / np.sum(confusion, axis=1)
    
    if train_mode:
        model.train()

    return accuracy, per_class_accuracy, confusion

def print_test_results(model):
    accuracy, per_class_accuracy, confusion = test_model(model)
    print(f'Global accuracy {accuracy:.2%}')
    print('Confusion matrix:')
    print(confusion)
    print('Per class accuracies:')
    for acc, name in zip(per_class_accuracy, targets):
        print(f'{name:>12}: {acc:.2%}')

def train_model(model, epochs):
    
    model.train()
    
    # construct name
    model_name = model.__class__.__name__
    optimizer_name = optimizer.__class__.__name__
    run_name = f'{model_name}-{optimizer_name}-lr{learning_rate}'
    
    # init weight and biases
    with wandb.init(project='DLL-Project', name=run_name) as run:
        
        # log some info
        run.config.learning_rate = learning_rate
        run.config.optimizer = optimizer.__class__.__name__
        run.watch(model)
        
        # progress bar
        mb = master_bar(range(epochs))
        
        for epoch in mb:
            
            for inputs, labels in progress_bar(iter(train_loader), parent=mb):

                # move the data to the GPU
                inputs, labels = inputs.to(device), labels.to(device)

                # set all parameter gradients to zero
                optimizer.zero_grad()

                # compute the forward pass
                outputs = model.forward(inputs)

                # compute loss and backpropagate gradients
                loss = criterion(outputs, labels)
                loss.backward()

                # update parameters
                optimizer.step()

                # log the loss
                run.log({'loss': loss})
                
            # evaluate the model
            accuracy, per_class_accuracy, confusion = test_model(model)
            mb.main_bar.comment = f'val acc:{accuracy}'

            # log the data
            run.log({'accuracy': accuracy, 'epoch': epoch})

epochs = 50
train_model(model, epochs)
print_test_results(model)
