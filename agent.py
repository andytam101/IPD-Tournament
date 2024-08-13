from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, agent_id, strategy) -> None:
        self.id = agent_id
        self.strategy = strategy
        self.interactions = 0

    @abstractmethod
    def play(self, agent_id):
        """Return False for Cooperate, True for Defect"""

    @abstractmethod
    def result(self, agent_id, self_choice, opponent_choice, points):
        """Receives the outcome"""

