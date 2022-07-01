import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

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

    '''
    - @nemo this is exactly your implementation of the lstm
    - Just added defaults for the constructor inputs
    - Focus on this class to make it trainable on sequences of length 10
    '''

    def __init__(self, input_size, num_classes=3, hidden_size=64, num_layers=1):

        super().__init__()
        self.num_classes = num_classes # number of classes
        self.num_layers = num_layers # number of layers
        self.input_size = input_size # input size
        self.hidden_size = hidden_size # hidden state
        # self.seq_length = seq_length # sequence length

        self.lstm = torch.nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, batch_first=True, dropout=0.25) 

        self.fc1 = nn.Linear(hidden_size, 100) 
        nn.init.kaiming_uniform_(self.fc1.weight, nonlinearity='relu')
        nn.init.constant_(self.fc1.bias, 0.0)       

        self.fc2 = nn.Linear(100, 50)
        nn.init.kaiming_uniform_(self.fc2.weight, nonlinearity='relu')
        nn.init.constant_(self.fc2.bias, 0.0)       
        self.dropout1 = nn.Dropout(p=0.5)

        self.fc3 = nn.Linear(50, num_classes)
        nn.init.xavier_uniform_(self.fc3.weight)
        nn.init.constant_(self.fc3.bias, 0.0) 
        
        self.relu = nn.ReLU()
    
    def forward(self,x):
        h_0 = Variable(torch.zeros(self.num_layers, x.size(0), self.hidden_size)) # hidden state
        c_0 = Variable(torch.zeros(self.num_layers, x.size(0), self.hidden_size)) # internal state
        
        # Propagate input through LSTM
        output, (hn, cn) = self.lstm(x, (h_0, c_0)) # lstm with input, hidden, and internal state
        hn = hn.view(-1, self.hidden_size) # reshaping the data for Dense layer next

        x = self.relu(hn)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.dropout1(x)
        x = F.sigmoid(self.fc3(x))
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
        return LSTM(input_size=dim_input)
    else:
        raise Exception('invalid model')

