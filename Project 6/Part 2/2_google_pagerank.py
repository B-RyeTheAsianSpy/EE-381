"""
Name:   Brian Nguyen
Class:  EE 381 - Probability & Stats
Start:  5/2/19
End:    5/3/19
"""

import numpy as np
import matplotlib.pyplot as plt

def nSidedDie(p):
    n = len(p)
    cs = np.cumsum(p)
    cp = np.append(0, cs)
    r = np.random.rand()
    for k in range(0, n):
        if r > cp[k] and r <= cp[k + 1]:
            d = k + 1
    return d - 1


def pagerank():
    n = 20
    initial = [0.2, 0.2, 0.2, 0.2, 0.2]
    stm0 = [0, 1, 0, 0, 0]          # A
    stm1 = [0.5, 0, 0.5, 0, 0]      # B
    stm2 = [1/3, 1/3, 0, 0, 1/3]    # C
    stm3 = [1, 0, 0, 0, 0]          # D
    stm4 = [0, 1/3, 1/3, 1/3, 0]    # E
    P = np.matrix([stm0,
                   stm1,
                   stm2,
                   stm3,
                   stm4])

    S = np.zeros((n, 5))
    S[0, :] = initial
    for k in range(1, n):
        S[k, :] = S[k - 1, :] * P

    b = list(range(0, n))
    fig1 = plt.figure(1)
    plt.plot(b, S[:, 0], '--*', label='State A')
    plt.plot(b, S[:, 1], '--o', label='State B')
    plt.plot(b, S[:, 2], '--h', label='State C')
    plt.plot(b, S[:, 3], '--x', label='State D')
    plt.plot(b, S[:, 4], '--+', label='State E')
    plt.title("Google PageRank Algorithm with probability distribution vector v1 = [1/5, 1/5, 1/5, 1/5, 1/5]")
    plt.xlabel("Step Number")
    plt.ylabel("State")
    plt.legend()
    print(S)
    plt.show()

    initial = [0, 0, 0, 0, 1]
    fig2 = plt.figure(2)
    S = np.zeros((n, 5))
    S[0, :] = initial
    for k in range(1, n):
        S[k, :] = S[k - 1, :] * P
    plt.plot(b, S[:, 0], '--*', label='State A')
    plt.plot(b, S[:, 1], '--o', label='State B')
    plt.plot(b, S[:, 2], '--h', label='State C')
    plt.plot(b, S[:, 3], '--x', label='State D')
    plt.plot(b, S[:, 4], '--+', label='State E')
    plt.title("Google PageRank Algorithm with probability distribution vector v2 = [0, 0, 0, 0, 1]")
    plt.xlabel("Step Number")
    plt.ylabel("State")
    plt.legend()
    print(S)
    plt.show()


def main():
    pagerank()


main()
