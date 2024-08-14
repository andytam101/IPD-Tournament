from agent import Agent


class Grim(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        Cooperates until opponent defects, then defect forever
        """
        super().__init__(agent_id, strategy)
        self.defected = set()

    def play(self, agent_id):
        return agent_id in self.defected
        
    def result(self, agent_id, self_choice, opponent_choice, points):
        if opponent_choice == 1:
            self.defected.add(agent_id)
    