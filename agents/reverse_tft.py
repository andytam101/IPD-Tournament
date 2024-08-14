from agent import Agent


class ReverseTFT(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        Like TFT, but does the opposite of what the opponent does
        """
        super().__init__(agent_id, strategy)
        self.history = {}

    def play(self, agent_id):
        if agent_id not in self.history:
            return 1
        else:
            return not self.history[agent_id]
    
    def result(self, agent_id, self_choice, opponent_choice, points):
        self.history[agent_id] = opponent_choice
        