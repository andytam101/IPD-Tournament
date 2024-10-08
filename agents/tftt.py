from agent import Agent

class TFTT(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        Starts off cooperating, then defect if opponent defected twice in a row
        """
        super().__init__(agent_id, strategy)
        self.history = {}
    
    def play(self, agent_id):
        if agent_id not in self.history:
            return 0
        else:
            return self.history[agent_id] >= 2
    
    def result(self, agent_id, self_choice, opponent_choice, points):
        if opponent_choice == 0:
            self.history[agent_id] = 0
        elif agent_id not in self.history:
            self.history[agent_id] = 1
        else:
            self.history[agent_id] += 1

