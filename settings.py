from factories import *

# constants
ITERATIONS = 1_000_000
DISPLAY_TOP_AGENTS = 10

# file paths
SAVED_GAMES = "saves/"

# strategy count
default_strategies_count = {
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
    buildHandShake: 20,
    buildMaster: 1,
    buildSlave: 19,
    buildPavlov: 10,
    buildAdaptiveTFT: 10,
    buildReverseTFT: 10,
    buildForgivingTFT: 10,
    buildQLearner: 1
}
