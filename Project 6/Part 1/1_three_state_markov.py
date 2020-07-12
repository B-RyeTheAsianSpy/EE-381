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


def markov():
    S = []
    initial = [0.25, 0, 0.75]
    stm1 = [1/2, 1/4, 1/4]
    stm2 = [1/4, 1/8, 5/8]
    stm3 = [1/3, 2/3, 0]
    for i in range(15):
        r = nSidedDie(initial)
        S.append(r)
    print("Initial states", S)
    for k in range(1, 15):
        if S[k - 1] == 0:
            S[k] = nSidedDie(stm1)
        elif S[k - 1] == 1:
            S[k] = nSidedDie(stm2)
        else:
            S[k] = nSidedDie(stm3)
    b = list(range(0, len(S)))
    print("Final states", S)
    plt.title("A sample simulation run of a three-state Markov Chain")
    plt.xlabel("Step Number")
    plt.ylabel("State")
    plt.plot(b, S, 'c:')
    plt.plot(b, S, 'bo', label="State")
    plt.legend()
    plt.show()


def markov_thousand():
    n = 15
    N = 10_000
    initial = [0.25, 0, 0.75]
    stm1 = [1 / 2, 1 / 4, 1 / 4]
    stm2 = [1 / 4, 1 / 8, 5 / 8]
    stm3 = [1 / 3, 2 / 3, 0]
    P = np.matrix([
                   stm1,
                   stm2,
                   stm3
                   ])
    S = np.zeros((n, 3))
    S[0, :] = initial
    for k in range(1, n):
        S[k, :] = S[k - 1, :] * P
    b = list(range(0, n))
    plt.plot(b, S[:, 0], 'b--*', label='Rain')
    plt.plot(b, S[:, 1], 'g--o', label='Nice')
    plt.plot(b, S[:, 2], 'c--h', label='Snow')
    plt.title("Three-state Markov Chain With State Transition Matrix")
    plt.xlabel("Step")
    plt.ylabel("State")
    plt.legend()
    plt.show()

    M = np.zeros((n, 3))
    S = np.array(np.zeros((n, N)))
    for k in range(0, N):
        r = nSidedDie(initial)
        S[0, k] = r

    for k in range(0, N):
        for j in range(1, n):
            current = S[j - 1, k]
            if current  == 0:
                r = nSidedDie(stm1)
            elif current  == 1:
                r = nSidedDie(stm2)
            else:
                r = nSidedDie(stm3)
            S[j, k] = r
    for j in range(0, n):
        u = S[j, :]
        r = 0
        n = 0
        s = 0
        for k in range(0, N):
            if u[k] == 0:
                r += 1
            elif u[k] == 1:
                n += 1
            else:
                s += 1
        M[j, :] = [r / N, n / N, s / N]
    plt.plot(M[:, 0], 'b--*', label='Rain')
    plt.plot(M[:, 1], 'g--o', label='Nice')
    plt.plot(M[:, 2], 'c--+', label='Snow')
    plt.title('Three-state Markov Chain Without State Transition Matrix')
    plt.xlabel('Step')
    plt.ylabel('State')
    plt.legend()
    plt.show()

def main():
    markov()
    markov_thousand()


main()
