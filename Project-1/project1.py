import numpy as np

import random
import string


import matplotlib
import matplotlib.pyplot as plt

def sum2dice(N):
    d1 = np.random.randint(1, 7, N)
    d2 = np.random.randint(1, 7, N)
    s = d1 + d2
    b = range(1, 5)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s, bins=b)
    b1 = bin_edges[0:sb-1]
    plt.close('all')

    fig = plt.figure(1)
    plt.stem(b1, h1)
    plt.title('Stem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# PROBLEM 1
# n-sided die
# Inputs: the probability for each side, given as a vector p = [p1, p2, ..., pn]
# Outputs: the number on the face of the die after a single roll, i.e. one number from the set of integers
def nSidedDie(p):
    # p = [0.10,  0.15,  0.20,  0.05,  0.30, 0.10, 0.10]
    n = len(p)
    cs = np.cumsum(p)
    cp = np.append(0, cs)
    r = np.random.rand()
    for k in range(0, n):
        if r > cp[k] and r <= cp[k + 1]:
            d = k + 1
    return d

def nSidedDieTester(N):
    theList = []
    for x in range(0, N):
        r = nSidedDie([0.10, 0.15, 0.20, 0.05, 0.30, 0.10, 0.10])
        theList.append(r)
    b = range(1, max(theList) + 2)
    sb = np.size(b)
    h1, bin_edges = np.histogram(theList, bins=b)
    b1 = bin_edges[0:sb - 1]
    plt.close('all')

    plt.figure(1)
    plt.stem(b1, h1)
    plt.title('n-sided die')
    plt.xlabel('Face rolled')
    plt.ylabel('# of times rolling the face')
    plt.show()



# PROBLEM 2
# Roll a pair of dice until you get a sum of 7, which is considered a "success"
# Track the number of rolls it takes to get a "success"
def sumOfSeven(N):
    roll = 0
    list = []
    for x in range(0, N):
        d1 = np.random.randint(1, 7)
        d2 = np.random.randint(1, 7)
        roll += 1
        s = d1 + d2
        # print(d1, "+", d2, "=", sum)
        if s == 7:
            list.append(roll)
            roll = 0
    print(list)
    b = range(1, 40)
    sb = np.size(b)
    h1, bin_edges = np.histogram(list, bins=b)
    b1 = bin_edges[0:sb - 1]
    plt.close('all')

    plt.figure(1)
    plt.stem(b1, h1)
    plt.title('Sum of 7')
    plt.xlabel('# of rolls')
    plt.ylabel('# of occurrences of that roll')
    plt.show()




# PROBLEM 3
# Toss 100 fair coins and record the number of "heads."
# If you get 50 heads, the experiment is considered a "success"
def fiftyHeads(N):
    success = 0
    for k in range(0, N):
        coin = np.random.randint(0, 2, 100)
        heads = sum(coin)
        if heads == 50:
            success += 1
    p_success = success / N
    print('probability of success = ', p_success)


# PROBLEM 4 - Password Hacking
# Your computer system uses a four letter password for login
# A hacker creates a list of m random 4-letter words as candidates for matching password
# You are going to check if the hacker's list contains at least one of word that matches your password
def passwordHack(N, m):
    random_string = string.ascii_letters.lower()
    my_password = 'seth'
    success = 0
    for a in range(0, N):
        print(a)
        hackers_list = []
        for x in range(m):
            random_password = ''.join(random.choice(random_string) for i in range(4))
            hackers_list.append(random_password)
        for q in range(0, len(hackers_list)):
            if hackers_list[q] == my_password:
                print('success!')
                success += 1
                break
    p_success = success/N
    print('probability of success = ', p_success)

def main():
    # Problem 1
    # nSidedDieTester(100000)

    # Problem 2
    # sumOfSeven(100000)

    # Problem 3
    # fiftyHeads(100000)

    #Problem 4
    passwordHack(1000, 80000)

main()