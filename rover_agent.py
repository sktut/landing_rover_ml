import numpy as np

class RoverAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.9):
        self.q_table = np.zeros((5, 5, 4))  # Example grid size and action space
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def choose_action(self, state):
        if np.random.rand() < 0.1:  # Epsilon-greedy strategy
            return np.random.randint(4)  # Explore
        return np.argmax(self.q_table[state])  # Exploit

    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.learning_rate * td_error
