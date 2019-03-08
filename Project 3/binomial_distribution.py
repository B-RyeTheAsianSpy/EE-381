import numpy as np
import matplotlib.pyplot as plt

# parameters:
#   number of trials, probability of success, repetition of experiment
s = np.random.binomial(1000, 0.003, size=10000)
b = range(0, 15)
sb = np.size(b)
h1, bin_edges = np.histogram(s, bins=b)
h1 = h1 / 10000
b1 = bin_edges[0:sb - 1]
plt.close('all')

plt.figure(2)
plt.stem(b1, h1)
plt.title('Bernoulli Trials: PMF - Binomial Formula')
plt.xlabel('Number of successes in n = 1000 trials')
plt.ylabel('Probability')
plt.show()