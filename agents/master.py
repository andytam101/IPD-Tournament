from agent import Agent


class Master(Agent):
    def __init__(self, agent_id, strategy) -> None:
        super().__init__(agent_id, strategy)
        self.masters = set()
        self.others  = set()
        self.history_count = {}
        self.history_master_count = {}

        self.master_handshake = (1, 1, 0, 1, 0)

    def play(self, agent_id):
        if agent_id in self.masters:
            return 0
        elif agent_id in self.history_count and self.history_count[agent_id] < 5:
            return self.master_handshake[self.history_count[agent_id]]
        else:
            return 1
    
    def result(self, agent_id, self_choice, opponent_choice, points):
        if agent_id not in self.history_count:
            self.history_count[agent_id] = 0

        self.history_count[agent_id] += 1

        if agent_id in self.others:
            return 
        if agent_id in self.masters:
            if opponent_choice == 1:
                self.masters.remove(agent_id)
                self.others.add(agent_id)
            return
        
        if agent_id not in self.history_master_count:
            self.history_master_count[agent_id] = 0
        if opponent_choice == self.master_handshake[self.history_master_count[agent_id]]:
            self.history_master_count[agent_id] += 1
            if self.history_master_count[agent_id] == 5:
                self.masters.add(agent_id)
        else:
            self.others.add(agent_id)

        
        
        

