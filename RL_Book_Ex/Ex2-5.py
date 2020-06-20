"""
Using non-stationary 10-armed bandit testbed
q_*(a) starts of as 1.
Then, each one takes an independent random walk,
    by adding a X~N(0,.01^2)
2 Agents: (\epsilon = .1) \alpha_n =
    1/n
    0.1
Plot graphs of action value against time-step (upto t = 10^4)
"""

import numpy as np
import random

class Bandit():
    def __init__(self):
        super().__init__()
        """
        initialise bandit ~N(0, 1^2)
        """
        self.value = np.random.normal()

    def get_reward(self):
        """
        Return a stochastic reward ~N(self.vale, 1^2)
        """
        return np.random.normal(loc=self.value)
    

class Agent():
    def __init__(self, epsilon=.1, alpha=lambda x: .1, k=10):
        super().__init__()
        """
        initialise RL agent
        """

        self.epsilon = epsilon
        self.alpha = alpha # Expected to be a lambda function
        self.Q_estimates = np.zeros((2, k))
        self.rewardLog = []

    def update_Q(self, banditNum, reward):
        """
        Increment count of Q
        Update estimate of Q
        """
        self.rewardLog.append(reward)
        self.Q_estimates[1][banditNum] += 1
        self.Q_estimates[0][banditNum] += self.alpha(self.Q_estimates[1][banditNum]) * (reward - self.Q_estimates[0][banditNum])
        
    def choose_bandit(self):
        """
        Return which bandit to use in interval (0, k - 1)
        based on epsilon-greedy method
        """
        
        if random.random() > self.epsilon:
            # Exploit
            # Get index of best Q-value
            action = np.argmax(self.Q_estimates[0])
        else:
            # Explore all possibilities with equal chance
            k = np.shape(self.Q_estimates)[1]
            action = random.randint(0, k)

        return action

def main():
    # Initialise 10 bandits, 2 agents
    # Plot graphs
    bandits = [Bandit() for i in range(10)]
    agents = [Agent(alpha=lambda x: 1/x), Agent()]

    for i in range(10000):
        for agent in agents:
            bandit = agent.choose_bandit()
            reward = bandits[bandit].get_reward()
            agent.update_Q(bandit, reward)



if __name__ == "__main__":
    main()
