import random
from collections import deque

import torch
import torch.nn as nn
import torch.optim as optim
from actions import Actions


class State:
    def __init__(self, player_action, opponent_action, player_delay, opponent_delay, score, time):
        self.player_action = player_action
        self.opponent_action = opponent_action
        self.player_delay = player_delay
        self.opponent_delay = opponent_delay
        self.score = score
        self.time = time


class DQN(nn.Module):
    def __init__(self, input_size, output_size):
        super(DQN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, output_size)
        )

    def forward(self, x):
        return self.network(x)


class BoxerAI:
    def __init__(self):
        self.state_size = 6
        self.action_size = 11
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = DQN(self.state_size, self.action_size).to(self.device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)

        self.last_state = None
        self.last_action = None

    def state_to_tensor(self, state):
        return torch.FloatTensor([
            state.player_action,
            state.opponent_action,
            state.player_delay,
            state.opponent_delay,
            state.score,
            state.time
        ]).to(self.device)

    def get_action(self, state):
        state = self.state_to_tensor(state)

        if random.random() < self.epsilon:
            action = random.choice(Actions.DECISIONS)
        else:
            with torch.no_grad():
                q_values = self.model(state)

                valid_actions = torch.zeros_like(q_values)
                for i, action in enumerate(Actions.DECISIONS):
                    valid_actions[i] = q_values[i]

                action = Actions.DECISIONS[torch.argmax(valid_actions).item()]

        self.last_state = state
        self.last_action = action

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

        return action

    def learn(self, new_state):
        if not self.last_state or not self.last_action:
            return

        reward = self.calculate_reward(new_state)

        new_state_tensor = self.state_to_tensor(new_state)

        self.memory.append((self.last_state, self.last_action, reward, new_state))

        if len(self.memory) >= 32:
            self.train()

    def calculate_reward(self, state):
        reward = 0

        if state.score > self.last_state[4]:
            reward += 10

        if (state.player_action == Actions.PUNCH_LEFT and state.opponent_action == Actions.DODGE_LEFT) \
                or (state.player_action == Actions.PUNCH_RIGHT and state.opponent_action == Actions.DODGE_RIGHT):
            reward += 5

        if state.score < self.last_state[4]:
            if state.opponent_action == Actions.BLOCK:
                reward -= 3
            else:
                reward -= 10

        return reward

    def train(self):
        batch = random.sample(self.memory, 32)

        for state, action, reward, next_state in batch:
            target = reward + self.gamma * torch.max(self.model(next_state).detach())

            current_q_values = self.model(state)
            target_q_values = current_q_values.clone()
            target_q_values[action] = target

            self.optimizer.zero_grad()
            loss = nn.MSELoss()(current_q_values, target_q_values)
            loss.backward()
            self.optimizer.step()
