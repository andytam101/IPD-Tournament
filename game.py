import random
from agent import Agent
from tqdm import tqdm


class Game:
    def __init__(self):
        self.agents = []

        # Both cooperate = 3
        # Both defect = 1
        # Defect = 5, Coop = 0
        self.payoff = [[3, 0], [5, 1]]
        self.info = {}

        self.total_iterations = 0

    def display_strategy_info(self):
        strategy_count = {}
        for a in self.agents:
            if a.strategy in strategy_count:
                strategy_count[a.strategy] += 1
            else:
                strategy_count[a.strategy] = 1

        for idx, s in enumerate(strategy_count):
            print(f"{idx + 1}. {s}: {strategy_count[s]}")

    def setup(self, factories):
        agent_id = 0
        for f in factories:
            for _ in range(factories[f]):
                self.agents.append(f(agent_id))
                # info: [points, number of interactions]
                self.info[agent_id] = [0, 0] 
                agent_id += 1

    def get_score(self, agent_id):
        return self.info[agent_id][0]
    
    def get_interactions(self, agent_id):
        return self.info[agent_id][1]

    def get_avg_score(self, agent_id):
        if self.get_interactions(agent_id) == 0:
            return 0
        else:
            return self.get_score(agent_id) / self.get_interactions(agent_id)

    def get_strategy(self, agent_id):
        return self.agents[agent_id].strategy

    def get_details(self, agent_id):
        return {
            "id": agent_id, 
            "strategy": self.get_strategy(agent_id),
            "score": self.get_score(agent_id),
            "interactions": self.get_interactions(agent_id),
            "average": self.get_avg_score(agent_id)
        }

    def top_n_agents(self, n, ranking="total"):
        """Returns top n performing agents based on score"""
        agent_ids = list(self.info.keys())
        agent_ids.sort(reverse=True, key=self.get_avg_score if ranking == "avg" else self.get_score)
        best = agent_ids[:n]

        result = map(self.get_details, best)
        return list(result)

    def strategies_ranking(self, ranking="total"):
        """Returns top n performing strategies based on average score"""
        # key = strategy name
        strategy_acc = {}

        for p in self.info:
            score = self.get_score(p)
            interactions = self.get_interactions(p)
            average = self.get_avg_score(p)
            strategy = self.get_strategy(p)
            
            if strategy in strategy_acc:
                strategy_acc[strategy][0] += score
                strategy_acc[strategy][1] += interactions
                strategy_acc[strategy][2] += average
                strategy_acc[strategy][3] += 1
            else:
                strategy_acc[strategy] = [score, interactions, average, 1]

        strategy_info = {}
        for strategy in strategy_acc:
            strategy_info[strategy] = [
                round(strategy_acc[strategy][0] / strategy_acc[strategy][3], 3), 
                round(strategy_acc[strategy][2] / strategy_acc[strategy][3], 3),
                strategy_acc[strategy][0]
            ]

        strategies = list(strategy_info.keys())
        strategies.sort(reverse=True, key=lambda x: strategy_info[x][1 if ranking=="avg" else 0])

        result = []
        
        for s in strategies:
            result.append({
                "strategy": s,
                "score per agent": strategy_info[s][0],
                "average score per agent": strategy_info[s][1],
                "total score": strategy_info[s][2]
            })

        return result

    def one_iteration(self):
        agents_copy = self.agents.copy()
        random.shuffle(agents_copy)

        midpoint = len(agents_copy) // 2
        first_half = agents_copy[:midpoint]
        second_half = agents_copy[midpoint:]

        pairs = zip(first_half, second_half)
        for p1, p2 in pairs:
            self.interact(p1, p2)

    def interact(self, p1: Agent, p2: Agent):
        p1_choice = p1.play(p2.id)
        p2_choice = p2.play(p1.id)

        p1_reward = self.payoff[p1_choice][p2_choice]
        p2_reward = self.payoff[p2_choice][p1_choice]

        p1.result(p2.id, p1_choice, p2_choice, p1_reward)
        p2.result(p1.id, p2_choice, p1_choice, p2_reward)

        self.info[p1.id][0] += p1_reward
        self.info[p1.id][1] += 1
        self.info[p2.id][0] += p2_reward
        self.info[p2.id][1] += 1

    def run(self, iterations):
        print(f"Playing {iterations} rounds with the current strategies...")
        self.display_strategy_info()
        print("=" * 100)
        for _ in tqdm(range(iterations), desc="Running"):
            self.one_iteration()
        
        self.total_iterations += iterations
