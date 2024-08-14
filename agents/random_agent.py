from agent import Agent
import random


class RandomAgent(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        Chooses cooperate / defect randomly
        """
        super().__init__(agent_id, strategy)

    def play(self, agent_id):
        return random.getrandbits(1)

    def result(self, agent_id, self_choice, opponent_choice, points):
        pass


