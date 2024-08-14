from agent import Agent


class AlwaysDefect(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        Always Defects
        """
        super().__init__(agent_id, strategy)

    def play(self, agent_id):
        return 1

    def result(self, agent_id, self_choice, opponent_choice, points):
        pass

