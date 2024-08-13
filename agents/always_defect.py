from agent import Agent


class AlwaysDefect(Agent):
    def play(self, agent_id):
        return 1

    def result(self, agent_id, self_choice, opponent_choice, points):
        pass

