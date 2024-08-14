from factories import *

# constants
ITERATIONS = 100_000
DISPLAY_TOP_AGENTS = 10

# strategy count
strategies_count = {
    buildAlwaysCoop: 10, 
    buildAlwaysDefect: 1, 
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
