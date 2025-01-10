import torch
import torch.nn as nn
import torch.optim as optim


class BoxerAI(nn.Module):
    def __init__(self, input_size=6, hidden_size=64, output_size=6):
        super(BoxerAI, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, hidden_size)
        self.output = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        return torch.softmax(self.output(x), dim=-1)
