from agent import Agent


class AdaptiveTFT(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        An adaption rate r is used to compute a continuous variable 'world' according to history moves of the opponent.
        world = world + r * (1 - world) if opponent cooperates
        world = world + r * (0 - world) if opponent defects
        Play cooperate if world >= 0.5 else defects
        """
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
    
