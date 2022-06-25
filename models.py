import torch
import torch.nn as nn
import torch.nn.functional as F

class MLP(nn.Module):

    def __init__(self, dim_input):
        super().__init__()
        self.fc1 = nn.Linear(dim_input, 50)
        self.fc2 = nn.Linear(50, 30)
        self.fc3 = nn.Linear(30, 10)
        self.fc4 = nn.Linear(10, 3)
        nn.init.kaiming_normal_(self.fc1.weight, nonlinearity='relu')
        nn.init.kaiming_normal_(self.fc2.weight, nonlinearity='relu')
        nn.init.kaiming_normal_(self.fc3.weight, nonlinearity='relu')
        nn.init.constant_(self.fc1.bias, 0.0)
        nn.init.constant_(self.fc2.bias, 0.0)
        nn.init.constant_(self.fc3.bias, 0.0)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x

class BuildingBlock(nn.Module):

    def __init__(self, dim_in, dim_out):
        super().__init__()
        self.fc1 = nn.Linear(dim_in, dim_in)
        self.fc2 = nn.Linear(dim_in, dim_out)
        self.fc3 = nn.Linear(dim_out, dim_out)
        self.shortcut = nn.Sequential()
        nn.init.kaiming_normal_(self.fc1.weight, nonlinearity='relu')
        nn.init.kaiming_normal_(self.fc2.weight, nonlinearity='relu')
        nn.init.kaiming_normal_(self.fc3.weight, nonlinearity='relu')
        nn.init.constant_(self.fc1.bias, 0.0)
        nn.init.constant_(self.fc2.bias, 0.0)
        nn.init.constant_(self.fc3.bias, 0.0)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        out = x + self.shortcut(x)
        out = F.relu(out)
        return out

class Shortcut(nn.Module):

    def __init__(self, dim_input):
        super().__init__()
        self.fc1 = nn.Linear(dim_input, 50)
        self.stack = nn.Sequential(*[BuildingBlock(50,30), BuildingBlock(30,10)])
        self.fc2 = nn.Linear(10, 3)
        nn.init.kaiming_normal_(self.fc1.weight, nonlinearity='relu')
        nn.init.constant_(self.fc1.bias, 0.0)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.stack(x)
        x = self.fc2(x)
        return x

class LSTM(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x

def get_model(args, dim_input):

    '''
    - Checks validity of requested model
    - Returns requested model
    '''

    if args.model == 'mlp':
        return MLP(dim_input)
    elif args.model == 'shortcut':
        return Shortcut(dim_input)
    elif args.model == 'lstm':
        return LSTM(dim_input)
    else:
        raise Exception('invalid model')

