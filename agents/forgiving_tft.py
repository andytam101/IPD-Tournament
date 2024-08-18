from agent import Agent
import random


class ForgivingTFT(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        Like TFT, but there is a chance it will still cooperate after being defected
        """
        super().__init__(agent_id, strategy)
        self.p = 0.1
        self.history = {}
    
    def play(self, agent_id):
        if agent_id not in self.history:
            return 0
        else:
            return random.random() > self.p and self.history[agent_id]

    
    def result(self, agent_id, self_choice, opponent_choice, points):
        self.history[agent_id] = opponent_choice
        