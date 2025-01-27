import random
from collections import deque

import torch
import torch.nn as nn
import torch.optim as optim
from actions import Actions


class State:
    def __init__(self, player_action, opponent_action, player_delay, opponent_delay, score):
        self.player_action = player_action
        self.opponent_action = opponent_action
        self.player_delay = player_delay
        self.opponent_delay = opponent_delay
        self.score = score


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
        self.action_size = len(Actions.DECISIONS)
        self.memory = deque(maxlen=10000)
        self.gamma = 0.9
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.0001
        self.batch_size = 64

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = DQN(self.state_size, self.action_size).to(self.device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)

        self.state_tensor = torch.zeros(self.state_size).to(self.device)
        self.last_state = None
        self.last_action = None

        self.model.apply(self.init_weights)

    @staticmethod
    def init_weights(layer):
        if isinstance(layer, nn.Linear):
            nn.init.xavier_uniform_(layer.weight)

    def state_to_tensor(self, state):
        self.state_tensor[0] = state.player_action / Actions.NUM_ACTIONS
        self.state_tensor[1] = state.opponent_action / Actions.NUM_ACTIONS
        self.state_tensor[2] = state.player_delay / 100
        self.state_tensor[3] = state.opponent_delay / 100
        self.state_tensor[4] = state.score / 50
        return self.state_tensor

    def get_action(self, state):
        state_tensor = self.state_to_tensor(state).unsqueeze(0).to(self.device)

        if random.random() < self.epsilon:
            action = random.choice(Actions.DECISIONS)
        else:
            with torch.no_grad():
                q_values = self.model(state_tensor)
                action = Actions.DECISIONS[torch.argmax(q_values).item()]

        self.last_state = state_tensor.clone()
        self.last_action = action

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

        return action

    def record_experience(self, new_state):
        if self.last_state is None or self.last_action is None:
            return

        reward = self.calculate_reward(new_state)

        new_state_tensor = self.state_to_tensor(new_state).unsqueeze(0).to(self.device)

        self.memory.append((self.last_state.clone(), self.last_action, reward, new_state_tensor.clone()))

    def calculate_reward(self, state):
        reward = 0

        score_diff = state.score - self.last_state[0][4] * 50

        if score_diff > 0:
            reward += 1

        elif score_diff < 0:
            reward -= 1

        if (state.player_action == Actions.PUNCH_LEFT and state.opponent_action == Actions.DODGE_RIGHT) \
                or (state.player_action == Actions.PUNCH_RIGHT and state.opponent_action == Actions.DODGE_LEFT):
            reward += 0.6

        if (state.player_action == Actions.DODGE_LEFT and state.opponent_action == Actions.PUNCH_RIGHT) \
                or (state.player_action == Actions.DODGE_RIGHT and state.opponent_action == Actions.PUNCH_LEFT):
            reward -= 0.2

        return reward

    def train(self, num_epochs=500):
        if len(self.memory) < self.batch_size:
            return

        for epoch in range(num_epochs):
            batch = random.sample(self.memory, self.batch_size)

            states, actions, rewards, next_states = zip(*batch)

            states = torch.cat(states).to(self.device)
            actions = torch.tensor([Actions.DECISIONS.index(a) for a in actions]).to(self.device)
            rewards = torch.tensor(rewards).to(self.device)
            next_states = torch.cat(next_states).to(self.device)

            current_q_values = self.model(states)
            predicted_q_values = current_q_values.gather(1, actions.unsqueeze(-1)).squeeze(-1)

            with torch.no_grad():
                max_next_q_values = self.model(next_states).max(1)[0]
                target_q_values = rewards + self.gamma * max_next_q_values

            print(f"Predicted Q-Values: {predicted_q_values[:5]}")
            print(f"Target Q-Values: {target_q_values[:5]}")

            loss = nn.MSELoss()(predicted_q_values.clamp(-1, 1), target_q_values.clamp(-1, 1))
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            print(f"Epoch {epoch + 1}/{num_epochs}, Avg Loss: {loss.item():.4f}")

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
