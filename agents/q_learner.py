from agent import Agent
import numpy as np
import random
import math


class QLearner(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        Reinforcement Q-Learning algorithm that allows the agent to learn and adapt their strategy against opponents
        """
        super().__init__(agent_id, strategy)
        self.seen = {}

        self.rounds_size = 3

        self.state = {}
        self.q_values = {}
    
        # constants
        self.learning_rate = 0.9
        self.discount_rate = 0.9
        self.epsilon_decay = 0.5
    
    def calculate_state(self, self_choice, opponent_choice):
        return 2 * self_choice + opponent_choice

    def get_state(self, agent_id):
        state = self.state[agent_id]
        return int(np.dot(np.power(4, np.arange(self.rounds_size)), state))
        
    def epsilon(self, agent_id):
        number_sa = 4 ** self.rounds_size * 2
        fraction = self.seen[agent_id] / number_sa
        return (1 - math.tanh(self.epsilon_decay * fraction))

    def new_agent(self, agent_id):
        self.seen[agent_id] = 0

        # initialise new Q-table
        self.q_values[agent_id] = np.zeros((4 ** self.rounds_size, 2))

        # initialise new state
        self.state[agent_id]    = np.zeros(self.rounds_size)

    def play(self, agent_id):
        if agent_id not in self.seen:
            self.new_agent(agent_id)

        # if random.random() > self.epsilon[agent_id]:
        if self.seen[agent_id] >= 4 and random.random() > self.epsilon(agent_id):
            # exploitation
            state = self.get_state(agent_id)
            result = np.argmax(self.q_values[agent_id][state])
        else:
            # exploration
            result = random.getrandbits(1)

        # decay epsilon
        # self.epsilon[agent_id] = max(self.epsilon_min, self.epsilon_decay * self.epsilon[agent_id])

        self.seen[agent_id] += 1
        return result
    
    
    def result(self, agent_id, self_choice, opponent_choice, points):
        # get old state
        old_state = self.get_state(agent_id)
    
        # update_state
        self.state[agent_id][:self.rounds_size - 1] = self.state[agent_id][1:]
        self.state[agent_id][self.rounds_size - 1]  = self.calculate_state(self_choice, opponent_choice)

        q_table = self.q_values[agent_id]

        # get new state
        new_state = self.get_state(agent_id)
        if self.seen[agent_id] > self.rounds_size:
            r = points
            max_q = np.max(q_table[new_state])
            temporal_difference = r + self.discount_rate * max_q - q_table[old_state, self_choice]
            q_table[old_state, self_choice] += self.learning_rate * temporal_difference
