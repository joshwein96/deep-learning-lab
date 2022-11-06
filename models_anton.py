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

    def __init__(self, input_size, device, num_classes=3, hidden_size=256, num_layers=1):

        super().__init__()
        self.num_classes = num_classes # number of classes
        self.num_layers = num_layers # number of layers
        self.input_size = input_size # input size
        self.hidden_size = hidden_size # hidden state
        self.device = device
        # self.seq_length = seq_length # sequence length

        self.lstm = torch.nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, batch_first=True) 

        self.dropout = nn.Dropout(0.25)

        self.fc1 = nn.Linear(hidden_size, 128)

        self.sigmoid = nn.ReLU()

        self.fc2 = nn.Linear(128, num_classes)
        
        self.softmax = nn.Softmax()

        '''
        self.fc1 = nn.Linear(hidden_size, num_classes) 
        #nn.init.kaiming_uniform_(self.fc1.weight)
        #nn.init.constant_(self.fc1.bias, 0.0)       

        self.fc2 = nn.Linear(128, num_classes)
        nn.init.xavier_uniform_(self.fc2.weight)
        nn.init.constant_(self.fc2.bias, 0.0)
        '''

    def forward(self,x):

        batch_size = x.size(0)

        # initialise hidden and internal states
        h_0 = Variable(torch.zeros(self.num_layers, batch_size, self.hidden_size)).requires_grad_().to(self.device)
        c_0 = Variable(torch.zeros(self.num_layers, batch_size, self.hidden_size)).requires_grad_().to(self.device)
        
        # Propagate input through LSTM
        # .detach() is used to ensure stable BPTT
        output, (hn, cn) = self.lstm(x, (h_0.detach(), c_0.detach()))
        last_output = output[:,-1, :]

        out = self.fc1(last_output)
        out = self.dropout(out)
        out = self.sigmoid(out)
        out = self.fc2(out)
        out = self.softmax(out)


        return out


def get_model(args, dim_input, device):

    '''
    - Checks validity of requested model
    - Returns requested model
    '''

    if args.model == 'mlp':
        return MLP(dim_input)
    elif args.model == 'shortcut':
        return Shortcut(dim_input)
    elif args.model == 'lstm':
        return LSTM(input_size=dim_input, device=device)
    else:
        raise Exception('invalid model')

