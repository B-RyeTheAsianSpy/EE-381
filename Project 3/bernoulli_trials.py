"""
Name:           Brian Nguyen
Class:          EE 381 - Probability and Stats
Date Assigned:  2/27/19
Date Finished:  3/8/19
"""

import numpy as np
import matplotlib.pyplot as plt


def bernoulli_trials(N):
    c = [1, 2, 3, 4, 5, 6]
    p = [0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
    n = 1000
    the_list = []
    success = 0
    for x in range(N):
        roll_1 = np.random.choice(c, n, p)
        roll_2 = np.random.choice(c, n, p)
        roll_3 = np.random.choice(c, n, p)
        for i in range(len(roll_1)):
            if roll_1[i] == 1 and roll_2[i] == 2 and roll_3[i] == 3:
                success += 1
        the_list.append(success)
        success = 0
    # ------------------------------------------------------------------
    b = range(0, 16)
    sb = np.size(b)
    h1, bin_edges = np.histogram(the_list, bins=b)
    h1 = h1 / N
    b1 = bin_edges[0:sb - 1]
    plt.close('all')

    plt.figure(1)
    plt.stem(b1, h1)
    plt.title('Bernoulli Trials: PMF - Experimental Results')
    plt.xlabel('Number of successes in n = 1000 trials')
    plt.ylabel('Probability')
    plt.show()


def main():
    bernoulli_trials(10000)
main()