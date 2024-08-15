from game import Game
from settings import *


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
        iterations=ITERATIONS
    )
    game.setup(strategies_count)
    game.display_game_info()
    print("=" * 100)
    game.run()
    top = game.top_n_agents(DISPLAY_TOP_AGENTS)
    print("=" * 100)
    display_top_n(top)
    print("=" * 100)
    strategies = game.strategies_ranking()
    display_strategy_ranking(strategies)


if __name__ == "__main__":
    main()
