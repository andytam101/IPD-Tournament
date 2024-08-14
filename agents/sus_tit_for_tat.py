from agent import Agent

class SuspiciousTitForTat(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        Starts off defecting, then copy opponent's last move
        """
        super().__init__(agent_id, strategy)
        self.history = {}

    def play(self, agent_id):
        if agent_id not in self.history:
            return 1
        else:
            return self.history[agent_id]

    def result(self, agent_id, self_choice, opponent_choice, points):
        self.history[agent_id] = opponent_choice
        