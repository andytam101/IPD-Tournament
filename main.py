from game import Game
from settings import *
from factories import factories_mapping
import pickle
import os
import argparse
import json


def get_factories(path):
    if path is None:
        return default_strategies_count

    # read json file
    f = open(path, "r")
    data = json.load(f)
    f.close()

    result = {}
    for s in data:
        result[factories_mapping[s]] = data[s]
    return result


def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--iteration", required=True, type=int)
    parser.add_argument("-l", "--load")
    parser.add_argument("-s", "--save")
    parser.add_argument("-a", "--agents")

    return parser.parse_args()


def load_game(path):
    with open(path, "rb") as f:
        game = pickle.load(f)
    return game


def save_game(game_obj, path):
    with open(path, "wb") as f:
        pickle.dump(game_obj, f, pickle.HIGHEST_PROTOCOL)


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
    args = get_arguments()

    if args.load is None:
        print("Starting new game...")
        game = Game()
        game.setup(get_factories(args.agents))
    else:
        try:
            with open(os.path.join(SAVED_GAMES, args.load), "rb") as f:
                game: Game = pickle.load(f)
            print(f"Loading game from: {os.path.join(SAVED_GAMES, args.load)}, which has ran for {game.total_iterations} total iterations")
            if args.agents is not None:
                new_agents = get_factories(args.agents)
                game.setup(new_agents)

        except FileNotFoundError:
            print("Input file not found")
            return
 
    print("=" * 100)
    game.run(args.iteration)
    top = game.top_n_agents(DISPLAY_TOP_AGENTS)
    print("=" * 100)
    display_top_n(top)
    print("=" * 100)
    strategies = game.strategies_ranking()
    display_strategy_ranking(strategies)
    if args.save is not None:
        print("=" * 100)
        print(f"Now saving game file to: {os.path.join(SAVED_GAMES, args.save)}")
        save_game(game, os.path.join(SAVED_GAMES, args.save))


if __name__ == "__main__":
    main()
