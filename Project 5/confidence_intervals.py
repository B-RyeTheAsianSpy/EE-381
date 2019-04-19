"""
Name:   Brian Nguyen
Class:  EE 381 - Probability & Stats
Start:  4/9/19
End:    4/19/19
"""



import numpy as np
import random
import matplotlib.pyplot as plt

N = 1_500_000   # population size
mu_x_gram = 55  # mean
sig_x_gram = 5  # standard deviation

def n95_upper(n, mu, sig):
    return mu + 1.96 * (sig / np.sqrt(n))


def n95_lower(n, mu, sig):
    return mu - 1.96 * (sig / np.sqrt(n))


def n99_upper(n, mu, sig):
    return mu + 2.58 * (sig / np.sqrt(n))


def n99_lower(n, mu, sig):
    return mu - 2.58 * (sig / np.sqrt(n))


def confidence(n):

    """
    :param n: size of sample
    :return: graphs depicting 95% and 99% confidence intervals
    """

    # 95% CONFIDENCE INTERVAL
    X_bar_list = []     # list to store values of X bar
    upper_list = []     # list to store values of upper bound graph
    lower_list = []     # list to store values
    B = np.random.normal(mu_x_gram, sig_x_gram, N)
    for i in range(n):
        if i == 0:
            i += 1
        X = B[random.sample(range(N), i)]
        X_bar = np.mean(X)
        X_bar_list.append(X_bar)    # store value of X_bar into list
        f1 = n95_upper(i, mu_x_gram, sig_x_gram)    # compute value for 95% confidence upper interval
        f2 = n95_lower(i, mu_x_gram, sig_x_gram)    # compute value for 95% confidence lower interval
        upper_list.append(f1)   # store upper limit value into list
        lower_list.append(f2)   # sotre lower limit value into list
    b = list(range(1, n + 1))
    plt.scatter(b, X_bar_list, color='b', marker='x', label='X_bar')
    plt.title('Sample means and 95% confidence interval')
    x_label = 'Sample size n = %d' % n
    plt.xlabel(x_label)
    plt.ylabel('X_bar')
    plt.plot(upper_list, 'r--', label='Upper bound')
    plt.plot(lower_list, 'r--', label='Lower bound')
    plt.legend()
    plt.show()
    # ----------------------------------------------------------
    # 99% CONFIDENCE INTERVAL
    X_bar_list = []
    upper_list = []
    lower_list = []
    for i in range(n):
        if i == 0:
            i += 1
        X = B[random.sample(range(N), i)]
        X_bar = np.mean(X)
        X_bar_list.append(X_bar)
        f1 = n99_upper(i, mu_x_gram, sig_x_gram)
        f2 = n99_lower(i, mu_x_gram, sig_x_gram)
        upper_list.append(f1)
        lower_list.append(f2)
    b = list(range(1, n + 1))
    plt.scatter(b, X_bar_list, color='b', marker='x', label='X_bar')
    plt.title('Sample means and 99% confidence interval')
    x_label = 'Sample size n = %d' % n
    plt.xlabel(x_label)
    plt.ylabel('X_bar')
    plt.plot(upper_list, 'g--', label='Upper bound')
    plt.plot(lower_list, 'g--', label='Lower bound')
    plt.legend()
    plt.show()


def main():
    n = int(input('Enter size n: '))
    confidence(n)

main()

