from game import Game
from factories import *


STRATEGIES = {
    buildAlwaysCoop: 10, 
    buildAlwaysDefect: 10, 
    buildRandom: 10,
    buildTitForTat: 10,
    buildSuspiciousTitForTat: 10,
    buildTFTT: 10,
    buildTTFT: 10,
    buildGrim: 10,
    buildProber: 10,
    buildSoftMajority: 10,
    buildHardMajority: 10,
    buildHandShake: 10,
    buildMaster: 1,
    buildSlave: 19,
    buildPavlov: 10,
    buildAdaptiveTFT: 10,
    buildQLearner: 1
}


def display_agent_info(agent):
    print(f"Agent {agent["id"]}: strategy='{agent["strategy"]}', score={agent["score"]}, score per interaction={agent["average"]}")


def display_strategy_ranking(strategies):
    print("Strategy Ranking: ")
    for idx, strategy in enumerate(strategies):
        print(f"{idx + 1}. {strategy["strategy"]}: average score = {strategy["score per agent"]}, average score per interaction = {strategy["average score per agent"]}")


def display_top_n(top_n):
    print(f"Agent Ranking (Top {len(top_n)}): ")
    for idx, agent in enumerate(top_n):
        print(f"{idx + 1}. ", end="")
        display_agent_info(agent)
        

def main():
    game = Game(
        iterations=100000
    )

    game.setup(STRATEGIES)
    game.run()
    top = game.top_n_agents(10)
    print("=" * 100)
    display_top_n(top)
    print("=" * 100)
    strategies = game.strategies_ranking()
    display_strategy_ranking(strategies)


if __name__ == "__main__":
    main()
