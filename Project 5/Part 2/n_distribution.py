"""
Name:   Brian Nguyen
Class:  EE 381 - Probability & Stats
Start:  4/19/19
End:    4/19/19
"""

import numpy as np
import random


N = 1_500_000   # population size
mu_x_gram = 55  # mean
sig_x_gram = 5  # standard deviation


def n_distribution(n):
    successes_n95 = 0
    successes_n99 = 0
    M = 10_000
    B = np.random.normal(mu_x_gram, sig_x_gram, N)
    for i in range(M):
        X = B[random.sample(range(N), n)]
        S = np.std(X, ddof=1)
        X_bar = np.mean(X)

        # compute values for limits
        ll_n95 = n_lower_limit_95(X_bar, S, n)
        ul_n95 = n_upper_limit_95(X_bar, S, n)
        ll_n99 = n_lower_limit_99(X_bar, S, n)
        ul_n99 = n_upper_limit_99(X_bar, S, n)
        if mu_x_gram >= ll_n95 and mu_x_gram <= ul_n95:
            successes_n95 += 1
        if mu_x_gram >= ll_n99 and mu_x_gram <= ul_n99:
            successes_n99 += 1
    successes_n95 = successes_n95 / M * 100
    successes_n99 = successes_n99 / M * 100
    print("Normal 95% confidence at n =", n, ":", successes_n95)
    print("Normal 99% confidence at n =", n, ":", successes_n99)


def n_lower_limit_95(X_bar, S, n):
    return X_bar - 1.96 * (S / np.sqrt(n))


def n_upper_limit_95(X_bar, S, n):
    return X_bar + 1.96 * (S / np.sqrt(n))


def n_lower_limit_99(X_bar, S, n):
    return X_bar - 2.78 * (S / np.sqrt(n))


def n_upper_limit_99(X_bar, S, n):
    return X_bar + 2.78 * (S / np.sqrt(n))


def main():
    n_distribution(5)
    n_distribution(40)
    n_distribution(120)

main()
