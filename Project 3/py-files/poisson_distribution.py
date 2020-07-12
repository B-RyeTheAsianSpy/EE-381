"""
Name:           Brian Nguyen
Class:          EE 381 - Probability and Stats
Date Assigned:  2/27/19
Date Finished:  3/8/19
"""

import numpy as np
import matplotlib.pyplot as plt

# parameters
#   expected number of successes, total trials
s = np.random.poisson(3, 1000)
b = range(0, 15)
sb = np.size(b)
h1, bin_edges = np.histogram(s, bins=b)
h1 = h1 / 1000
b1 = bin_edges[0:sb - 1]
plt.close('all')

plt.figure(3)
plt.stem(b1, h1)
plt.title('Bernoulli Trials: PMF - Poisson Approximation')
plt.xlabel('Number of successes in n = 1000 trials')
plt.ylabel('Probability')
plt.show()