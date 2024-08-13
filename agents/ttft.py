from agent import Agent

class TTFT(Agent):
    def __init__(self, agent_id, strategy) -> None:
        super().__init__(agent_id, strategy)
        self.history = {}
    
    def play(self, agent_id):
        if agent_id not in self.history:
            return 0
        else:
            return self.history[agent_id] > 0
    
    def result(self, agent_id, self_choice, opponent_choice, points):
        if opponent_choice == 1:
            self.history[agent_id] = 2
        elif agent_id not in self.history:
            self.history[agent_id] = 0 
        else:
            self.history[agent_id] -= 1
            
