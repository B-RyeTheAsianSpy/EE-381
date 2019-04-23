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

def t_distribution(n):
    successes_t95 = 0
    successes_t99 = 0
    M = 10_000
    B = np.random.normal(mu_x_gram, sig_x_gram, N)
    for i in range(M):
        # all t values from the student's t chart
        if n == 5:
            t_95 = 2.78
            t_99 = 4.60
        elif n == 40:
            t_95 = 2.02
            t_99 = 2.71
        elif n == 120:
            t_95 = 1.98
            t_99 = 2.62
        else:
            break
        X = B[random.sample(range(N), n)]
        S = np.std(X, ddof=1)
        X_bar = np.mean(X)

        # compute values for limits
        ll_t95 = t_lower_limit(X_bar, S, n, t_95)
        ul_t95 = t_upper_limit(X_bar, S, n, t_95)
        ll_t99 = t_lower_limit(X_bar, S, n, t_99)
        ul_t99 = t_upper_limit(X_bar, S, n, t_99)
        if mu_x_gram >= ll_t95 and mu_x_gram <= ul_t95:
            successes_t95 += 1
        if mu_x_gram >= ll_t99 and mu_x_gram <= ul_t99:
            successes_t99 += 1
    successes_t95 = successes_t95 / M * 100
    successes_t99 = successes_t99 / M * 100
    print("Student t 95% confidence at n =", n, ":", successes_t95)
    print("Student t 99% confidence at n =", n, ":", successes_t99)


def t_lower_limit(X_bar, S, n, t):
    return X_bar - t * (S / np.sqrt(n))


def t_upper_limit(X_bar, S, n, t):
    return X_bar + t * (S / np.sqrt(n))


def main():
    t_distribution(5)
    t_distribution(40)
    t_distribution(120)


main()


