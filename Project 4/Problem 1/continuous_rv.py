"""
Name:           Brian Nguyen
Class:          EE 381 - Probability & Stats
Start Date:     3/14/19
End Date:       3/15/19
"""

import numpy as np
import matplotlib.pyplot as plt


def uniform_rv():
    print('---------------\nUNIFORM RV')
    # Generate the values of the RV X
    a = 1
    b = 4
    n = 10000
    x = np.random.uniform(a, b, n)

    # Create bins and histogram
    nbins = 30
    edgecolor = 'w'
    bins = [float(x) for x in np.linspace(a, b, nbins+1)]
    h1, bin_edges = np.histogram(x,bins,density=True)

    # Define points on the horizontal axis

    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth=b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')

    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

    # PLOT THE UNIFORM PDF
    f = unif_pdf(1, 4, b1)
    plt.plot(b1, f, 'r')
    plt.title('Uniform RV Simulation')
    plt.xlabel('n = 1000')
    plt.ylabel('Probability')
    plt.show()

    # CALCULATE THE MEAN AND STANDARD DEVIATION
    mu_x = np.mean(x)
    sig_x = np.std(x)

    print('mu_x = ', mu_x)
    print('sig_x = ', sig_x)


def exponential_rv():
    print('---------------\nEXPONENTIAL RV')
    beta = 40
    n = 10000
    t = np.random.exponential(beta, n)
    nbins = 30
    edgecolor = 'w'
    bins = [float(t) for t in np.linspace(0, 200, nbins + 1)]
    h1, bin_edges = np.histogram(t, bins, density=True)

    # Define points on the horizontal axis

    be1 = bin_edges[0:np.size(bin_edges) - 1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]  # Width of bars in the bargraph
    plt.close('all')

    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)

    # PLOT THE UNIFORM PDF
    f = exp_pdf(beta, b1)
    plt.plot(b1, f, 'r')
    plt.title('Exponential RV Simulation')
    plt.xlabel('n = 1000')
    plt.ylabel('Probability')
    plt.show()

    # CALCULATE THE MEAN AND STANDARD DEVIATION
    mu_t = np.mean(t)
    sig_t = np.std(t)

    print('mu_t = ', mu_t)
    print('sig_t = ', sig_t)

def normal_rv():
    print('---------------\nNORMAL RV')
    mu = 2.5
    sigma = 0.75
    n = 10000
    x = np.random.normal(mu, sigma, n)
    nbins = 30
    edgecolor = 'w'
    bins = [float(x) for x in np.linspace(1, 4, nbins+1)]
    h1, bin_edges = np.histogram(x,bins,density=True)

    # Define points on the horizontal axis
    be1=bin_edges[0:np.size(bin_edges)-1]
    be2=bin_edges[1:np.size(bin_edges)]
    b1=(be1+be2)/2
    barwidth = b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')

    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

    # PLOT THE UNIFORM PDF
    f = normal_pdf(mu, sigma, b1)
    plt.plot(b1, f, 'r')
    plt.title('Normal RV Simulation')
    plt.xlabel('n = 1000')
    plt.ylabel('Probability')
    plt.show()

    # CALCULATE THE MEAN AND STANDARD DEVIATION
    mu_x = np.mean(x)
    sig_x = np.std(x)

    print('mu_x = ', mu_x)
    print('sig_x = ', sig_x)


# PLOT THE UNIFORM PDF
def unif_pdf(a,b,x):
    f = (1/abs(b-a))*np.ones(np.size(x))
    return f


# PLOT THE EXPONENTIAL PDF
def exp_pdf(beta, t):
    f = np.exp((-1 / beta) * t) * (1 / beta)
    return f


# PLOT THE NORMAL PDF
def normal_pdf(mu, sig, z):
    f = np.exp(-(z - mu) ** 2 / (2 * sig ** 2)) / (sig * np.sqrt(2 * np.pi))
    return f


def main():
    uniform_rv()
    exponential_rv()
    normal_rv()


main()

