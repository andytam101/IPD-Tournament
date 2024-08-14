from agent import Agent


class AlwaysCoop(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        Always Cooperates
        """
        super().__init__(agent_id, strategy)

    def play(self, agent_id):
        return 0

    def result(self, agent_id, self_choice, opponent_choice, points):
        pass
