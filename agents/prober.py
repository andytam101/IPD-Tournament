from agent import Agent


class Prober(Agent):
    def __init__(self, agent_id, strategy) -> None:
        super().__init__(agent_id, strategy)
        self.sequence = (1, 0, 0)
        self.start_history = {}
        self.tft_history = {}
        self.always_defect = set()

    def play(self, agent_id):
        if agent_id in self.always_defect:
            return 1

        if agent_id in self.tft_history:
            return self.tft_history[agent_id]
        
        if agent_id not in self.start_history:
            return self.sequence[0]
        else:
            return self.sequence[len(self.start_history[agent_id])]
    

    def result(self, agent_id, self_choice, opponent_choice, points):
        if agent_id in self.tft_history:
            self.tft_history[agent_id] = opponent_choice
            return
    
        if agent_id in self.always_defect:
            return

        if agent_id not in self.start_history:
            self.start_history[agent_id] = [opponent_choice]
        elif len(self.start_history[agent_id]) == 2:
            # completed 3 moves
            if self.start_history[agent_id][1] == 0 and opponent_choice == 0:
                # becomes always defect
                self.always_defect.add(agent_id)
            else:
                # becomes TFT
                self.tft_history[agent_id] = opponent_choice
        else:
            self.start_history[agent_id].append(opponent_choice)
        