from factories import *


TEST_ID = 1


# agent = buildQLearner(0)
# choice = agent.play(TEST_ID)
# print(int(choice))
# agent.result(TEST_ID, choice, 0, 1)
# choice = agent.play(TEST_ID)
# print(int(choice))
# agent.result(TEST_ID, choice, 0, 1)
# choice = agent.play(TEST_ID)
# print(int(choice))
# agent.result(TEST_ID, choice, 1, 1)
# choice = agent.play(TEST_ID)
# print(int(choice))
# agent.result(TEST_ID, choice, 0, 1)
# choice = agent.play(TEST_ID)
# print(int(choice))
# agent.result(TEST_ID, choice, 0, 1)
# choice = agent.play(TEST_ID)
# print(int(choice))
# agent.result(TEST_ID, choice, 1, 1)
# choice = agent.play(TEST_ID)
# print(int(choice))
# agent.result(TEST_ID, choice, 0, 1)
# choice = agent.play(TEST_ID)
# print(int(choice))


def calculate_reward(c0, c1):
    return [[3, 0], [5, 1]][c0][c1]


def one_round(display=True):
    c0 = int(agent_0.play(1))
    c1 = int(agent_1.play(0))

    a0 = calculate_reward(c0, c1)
    a1 = calculate_reward(c1, c0)

    agent_0.result(1, c0, c1, a0)
    agent_1.result(0, c1, c0, a1)

    if display:
        print(f"{agent_0.strategy}: {c0}, {agent_1.strategy}: {c1}, score={a0}")


agent_0 = buildQLearner(0)
agent_1 = buildRandom(1)

for _ in range(10000):
    # print("=" * 100)
    one_round(display=False)
    # print(agent_0.q_values[1])
    # print("=" * 100)

    # print(f"{agent_0.state[1]}: {agent_0.get_state(1)}")

for _ in range(1000):
    one_round()
