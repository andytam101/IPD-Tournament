from agent import Agent
import random


class RandomAgent(Agent):
    def play(self, agent_id):
        return random.getrandbits(1)

    def result(self, agent_id, self_choice, opponent_choice, points):
        pass


