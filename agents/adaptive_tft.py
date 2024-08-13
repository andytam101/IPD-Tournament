from agent import Agent


class AdaptiveTFT(Agent):
    def __init__(self, agent_id, strategy) -> None:
        super().__init__(agent_id, strategy)
        self.r = 0.2
        self.world = {}

    def play(self, agent_id):
        if agent_id not in self.world:
            return 0
        else:
            return self.world[agent_id] < 0.5

    def result(self, agent_id, self_choice, opponent_choice, points):
        if agent_id not in self.world:
            self.world[agent_id] = 0.5
        self.world[agent_id] = self.world[agent_id] + self.r * ((not opponent_choice) - self.world[agent_id])
    
