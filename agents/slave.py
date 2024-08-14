from agent import Agent


class Slave(Agent):
    def __init__(self, agent_id, strategy) -> None:
        """
        The master agent has a secret handshake agent. If the opponent follows the handshake signal, identify them as the master.
        Cooperate with master, defect against everyone else.
        """
        super().__init__(agent_id, strategy)
        self.masters = set()
        self.others = set()
        self.history_count = {}
        self.master_handshake = (1, 1, 0, 1, 0)

    def play(self, agent_id):
        if agent_id in self.masters:
            return 0
        elif agent_id in self.others:
            return 1
        else:
            return 0
        
    
    def result(self, agent_id, self_choice, opponent_choice, points):
        if agent_id in self.others:
            return 
        if agent_id in self.masters:
            if opponent_choice == 0:
                self.masters.remove(agent_id)
                self.others.add(agent_id)
            return
        
        if agent_id not in self.history_count:
            self.history_count[agent_id] = 0
        
        if opponent_choice == self.master_handshake[self.history_count[agent_id]]:
            self.history_count[agent_id] += 1
            if self.history_count[agent_id] == 5:
                self.masters.add(agent_id)
        else:
            self.others.add(agent_id)
