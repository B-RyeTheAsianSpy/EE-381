"""
Name:   Brian Nguyen
Class:  EE 381 - Probability & Stats
Start:  5/1/19
End:    5/1/19
"""


import numpy as np


def nSidedDie(p):
    n = len(p)
    cs = np.cumsum(p)
    cp = np.append(0, cs)
    r = np.random.rand()
    for k in range(0, n):
        if r > cp[k] and r <= cp[k + 1]:
            d = k + 1
    return d - 1


def absorption():
    S = []
    N = 10_000
    initial = [0, 0, 1, 0, 0]
    stm0 = [1, 0, 0, 0, 0]
    stm1 = [0.3, 0, 0.7, 0, 0]
    stm2 = [0, 0.5, 0, 0.5, 0]
    stm3 = [0, 0, 0.6, 0, 0.4]
    stm4 = [0, 0, 0, 0, 1]
    z, f = 0, 0
    for o in range(N):
        for i in range(15):
            r = nSidedDie(initial)
            S.append(r)
        for k in range(1, 15):
            if S[k - 1] == 0:
                S[k] = nSidedDie(stm0)
            elif S[k - 1] == 1:
                S[k] = nSidedDie(stm1)
            elif S[k - 1] == 2:
                S[k] = nSidedDie(stm2)
            elif S[k - 1] == 3:
                S[k] = nSidedDie(stm3)
            else:
                S[k] = nSidedDie(stm4)

        if 4 in S:
            z += 1
        elif 0 in S:
            f += 1
        S = []
    print("P(ending at b_20) = ", z / N)
    print("P(ending at b_24) = ", f / N)


def main():
    absorption()


main()
