class RoverEnvironment:
    def __init__(self):
        self.state = (0, 0)  # Example starting position

    def reset(self):
        self.state = (0, 0)
        return self.state

    def step(self, action):
        # Define how actions affect the rover's state and return next state and reward
        # For simplicity, just an example transition and reward
        if action == 0:  # Move up
            self.state = (max(0, self.state[0] - 1), self.state[1])
        elif action == 1:  # Move down
            self.state = (min(4, self.state[0] + 1), self.state[1])
        elif action == 2:  # Move left
            self.state = (self.state[0], max(0, self.state[1] - 1))
        elif action == 3:  # Move right
            self.state = (self.state[0], min(4, self.state[1] + 1))

        reward = -1  # Example reward for each step
        if self.state == (4, 4):  # Example success condition
            reward = 10  # Reward for landing successfully

        return self.state, reward
