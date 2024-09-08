from agents.always_coop import AlwaysCoop
from agents.always_defect import AlwaysDefect
from agents.random_agent import RandomAgent
from agents.tit_for_tat import TitForTat
from agents.sus_tit_for_tat import SuspiciousTitForTat
from agents.tftt import TFTT
from agents.ttft import TTFT
from agents.grim import Grim
from agents.prober import Prober
from agents.soft_majority import SoftMajority
from agents.hard_majority import HardMajority
from agents.handshake import HandShake
from agents.master import Master
from agents.slave import Slave
from agents.pavlov import Pavlov
from agents.adaptive_tft import AdaptiveTFT
from agents.reverse_tft import ReverseTFT
from agents.forgiving_tft import ForgivingTFT
from agents.q_learner import QLearner


def buildAlwaysCoop(agent_id):
    return AlwaysCoop(agent_id, "Always Coop")


def buildAlwaysDefect(agent_id):
    return AlwaysDefect(agent_id, "Always Defect")


def buildRandom(agent_id):
    return RandomAgent(agent_id, "Random")


def buildTitForTat(agent_id):
    return TitForTat(agent_id, "Tit for Tat")


def buildSuspiciousTitForTat(agent_id):
    return SuspiciousTitForTat(agent_id, "Suspicious TFT")


def buildTFTT(agent_id):
    return TFTT(agent_id, "TF2T")


def buildTTFT(agent_id):
    return TTFT(agent_id, "2TFT")


def buildGrim(agent_id):
    return Grim(agent_id, "Grim")


def buildProber(agent_id):
    return Prober(agent_id, "Prober")


def buildSoftMajority(agent_id):
    return SoftMajority(agent_id, "Soft Majority")


def buildHardMajority(agent_id):
    return HardMajority(agent_id, "Hard Majority")


def buildHandShake(agent_id):
    return HandShake(agent_id, "Handshake")


def buildMaster(agent_id):
    return Master(agent_id, "Master")


def buildSlave(agent_id):
    return Slave(agent_id, "Slave")


def buildPavlov(agent_id):
    return Pavlov(agent_id, "Pavlov")


def buildAdaptiveTFT(agent_id):
    return AdaptiveTFT(agent_id, "Adaptive TFT")


def buildReverseTFT(agent_id):
    return ReverseTFT(agent_id, "Reverse TFT")


def buildForgivingTFT(agent_id):
    return ForgivingTFT(agent_id, "Forgiving TFT")


def buildQLearner(agent_id):
    return QLearner(agent_id, "Q-Learner")


factories_mapping = {
    "ALCP": buildAlwaysCoop,
    "ALDF": buildAlwaysDefect,
    "RAND": buildRandom,
    "TFT": buildTitForTat,
    "TF2T": buildTFTT,
    "2TFT": buildTTFT,
    "RTFT": buildReverseTFT,
    "GRIM": buildGrim,
    "PAVL": buildPavlov,
    "PROB": buildProber,
    "STFT": buildSuspiciousTitForTat,
    "FTFT": buildForgivingTFT,
    "ATFT": buildAdaptiveTFT,
    "HAND": buildHandShake,
    "SMAJ": buildSoftMajority,
    "HMAJ": buildHardMajority,
    "MSTR": buildMaster,
    "SLVE": buildSlave,
    "QLRN": buildQLearner,
}