from agent import Agent


class Pavlov(Agent):
    def __init__(self, agent_id, strategy) -> None:
        super().__init__(agent_id, strategy)
        self.choice = {}

    def play(self, agent_id):
        if agent_id not in self.choice:
            return 0 
        else:
            return self.choice[agent_id]

    def result(self, agent_id, self_choice, opponent_choice, points):
        if agent_id not in self.choice:
            self.choice[agent_id] = not (opponent_choice == 0)
        elif opponent_choice == 1:
            self.choice[agent_id] = not self.choice[agent_id]
