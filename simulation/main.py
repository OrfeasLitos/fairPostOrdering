from pvs import PVS
import matplotlib.pyplot as plt
from utils import Utils

honestNo = 100
selfishMax = 100
a = 1/50
b = 0.0001
regen_time = 3 / (5*24*60*60) # as in Steem
att_span = 10
noRound = 20000
choice = 1 # 0 for uniform, 1 for beta
handicap = 1

def main():
    sybil_size = []
    gains = []
    for i in range(1, selfishMax):
        print("selfish:", i)
        noProfiles = (100, i, 0)
        sp = (1,) * sum(noProfiles)
        gain = PVS(noProfiles, sp, a, b, regen_time,
              att_span, noRound, choice, handicap).execute(output = False)

        sybil_size.append(i)
        gains.append(gain)

    Utils.plot_and_save(sybil_size, gains, "Voting ring size", "positions gained")

if __name__== "__main__":
    main()
