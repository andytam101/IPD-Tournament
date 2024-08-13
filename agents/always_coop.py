from agent import Agent


class AlwaysCoop(Agent):
    def play(self, agent_id):
        return 0

    def result(self, agent_id, self_choice, opponent_choice, points):
        pass
