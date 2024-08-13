from agent import Agent
import numpy as np
import random


class QLearner(Agent):
    def __init__(self, agent_id, strategy) -> None:
        super().__init__(agent_id, strategy)
        self.seen = {}

        self.rounds_size = 2

        self.state = {}
        self.q_values = {}
    
        # constants
        self.learning_rate = 0.
        self.discount_rate = 0.9
        self.epsilon       = 0.1

        # epsilon
        # self.epsilon       = {}
        # self.epsilon_init  = 0.9
        # self.epsilon_decay = 0.99
        # self.epsilon_min   = 0.1

    def normalise_reward(self, reward):
        mean = np.mean((0, 1, 3, 5))
        std  = np.std((0, 1, 3, 5))
        return (reward - mean) / std

    def calculate_state(self, self_choice, opponent_choice):
        return 2 * self_choice + opponent_choice

    def get_state(self, agent_id):
        state = self.state[agent_id]
        return int(np.dot(np.power(4, np.arange(self.rounds_size)), state))
        

    def new_agent(self, agent_id):
        self.seen[agent_id] = 0

        # initialise new Q-table
        self.q_values[agent_id] = np.zeros((4 ** self.rounds_size, 2))

        # initialise new state
        self.state[agent_id]    = np.zeros(self.rounds_size)

        # initialise new epsilon
        # self.epsilon[agent_id] = self.epsilon_init
    

    def play(self, agent_id):
        if agent_id not in self.seen:
            self.new_agent(agent_id)

        # if random.random() > self.epsilon[agent_id]:
        if self.seen[agent_id] < 4 or random.random() > self.epsilon:
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

        # get new state
        new_state = self.get_state(agent_id)

        if self.seen[agent_id] >= 4:
            self.q_values[agent_id][old_state, self_choice] = self.q_values[agent_id][old_state, self_choice] + self.learning_rate * (
                self.normalise_reward(points) - self.discount_rate * np.max(self.q_values[agent_id][new_state]) - self.q_values[agent_id][old_state,self_choice]
            )
        