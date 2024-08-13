from agent import Agent

class HandShake(Agent):
    def __init__(self, agent_id, strategy) -> None:
        super().__init__(agent_id, strategy)
        self.handshake = [0, 0, 1, 0]
        self.history_count = {}
        self.team = set()
        self.enemy = set()

    def play(self, agent_id):
        if agent_id in self.enemy:
            return 1
        elif agent_id in self.team:
            return 0
        elif agent_id not in self.history_count:
            return self.handshake[0]
        else:
            return self.handshake[self.history_count[agent_id]]
        
    def result(self, agent_id, self_choice, opponent_choice, points):
        if agent_id in self.enemy:
            return

        if self_choice != opponent_choice:
            self.enemy.add(agent_id)
            return
        
        if agent_id in self.team:
            return
    
        if agent_id not in self.history_count:
            self.history_count[agent_id] = 1
        else:
            self.history_count[agent_id] += 1
        
        if self.history_count[agent_id] == 4:
            self.team.add(agent_id)

