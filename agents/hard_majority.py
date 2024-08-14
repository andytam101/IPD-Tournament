from agent import Agent


class HardMajority(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        Starts off defect, then cooperate if opponent's cooperate count > opponent's defect count
        """
        super().__init__(agent_id, strategy)
        self.defect_count = {}

    def play(self, agent_id):
        if agent_id not in self.defect_count:
            return 1
        else:
            return self.defect_count[agent_id] <= 0
    
    def result(self, agent_id, self_choice, opponent_choice, points):
        if agent_id not in self.defect_count:
            self.defect_count[agent_id] = 0
        
        points = -opponent_choice * 2 + 1
        self.defect_count[agent_id] += points
    
    