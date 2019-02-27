import numpy as np
import matplotlib.pyplot as plt

p0 = 0.6
e0 = 0.05
e1 = 0.03

def errorTransmission(N):
    sList = []
    rList = []
    for x in range(N):
        S = nSidedDie([p0, 1 - p0])
        S = S - 1
        sList.append(S)
        if S == 1:
            R = nSidedDie([e1, 1 - e1])
            R = R - 1
            rList.append(R)
        elif S == 0:
            R = nSidedDie([1 - e0, e0])
            R = R - 1
            rList.append(R)
    # print('S = ', sList)
    # print('R = ', rList)
    fail_count = 0
    for k in range(0, len(sList)):
        if sList[k] != rList[k]:
            fail_count += 1
    print('-------\nRegular transmission\nprobability of failure', fail_count/N)
    # b = range(0, max(rList) + 2)
    # sb = np.size(b)
    # h1, bin_edges = np.histogram(sList, bins=b)
    # b1 = bin_edges[0:sb - 1]
    # plt.close('all')
    #
    # plt.figure(1)
    # plt.stem(b1, h1)
    # plt.title('n-sided die')
    # plt.xlabel('Face rolled')
    # plt.ylabel('# of times rolling the face')
    # plt.show()

def conditionalProbability(N):
    print('-------\nP(R = 1 | S = 1)\nCalculating...')
    sList = []
    rList = []
    for x in range(0, N):
        S = nSidedDie([p0, 1 - p0])
        S = S - 1
        sList.append(S)
        if S == 1:
            # epsilon 1 = 0.03
            R = nSidedDie([e1, 1 - e1])
            R = R - 1
            rList.append(R)
        elif S == 0:
            # epsilon 0 = 0.05
            R = nSidedDie([1 - e0, e0])
            R = R - 1
            rList.append(R)
    print('S =', sList)
    print('R =', rList)
    success = 0
    for k in range(len(sList)):
        if sList[k] == 1:
            if rList[k] == 1:
                success += 1
    one_count = sList.count(1)
    print("p =", success / one_count)

def conditionalProbability2(N):
    print('-------\nP(S = 1 | R = 1)\nCalculating...')
    sList = []
    rList = []
    for x in range(0, N):
        S = nSidedDie([p0, 1 - p0])
        S = S - 1
        sList.append(S)
        if S == 1:
            # epsilon 1 = 0.03
            R = nSidedDie([e1, 1 - e1])
            R = R - 1
            rList.append(R)
        elif S == 0:
            # epsilon 0 = 0.05
            R = nSidedDie([1 - e0, e0])
            R = R - 1
            rList.append(R)
    print('S =', sList)
    print('R =', rList)
    success = 0
    for k in range(len(sList)):
        if rList[k] == 1:
            if sList[k] == 1:
                success += 1
    one_count = rList.count(1)
    print("p =", success / one_count)


def enhancedTransmission(N):
    print('-------\nEnhanced Transmission\nCalculating...')
    sList = []
    rList = []
    for x in range(N):
        S = nSidedDie([p0, 1 - p0])
        S = S - 1
        if S == 1:
            sublist = [1, 1, 1]
            sList.append(sublist)
            sublist = []
            for i in range(3):
                R = nSidedDie([e1, 1 - e1])
                R -= 1
                sublist.append(R)
            rList.append(sublist)

        elif S == 0:
            sublist = [0, 0, 0]
            sList.append(sublist)
            sublist = []
            for i in range(3):
                R = nSidedDie([1 - e0, e0])
                R -= 1
                sublist.append(R)
            rList.append(sublist)
    # print(sList)
    # print(rList)
    fail = 0
    for k in range(len(sList)):
        r_count_zero = rList[k].count(0)
        r_count_one = rList[k].count(1)
        if sList[k] == [0, 0, 0]:
            if r_count_one > r_count_zero:
                fail += 1
        elif sList[k] == [1, 1, 1]:
            if r_count_zero > r_count_one:
                fail += 1
    print('probability of failure = ', fail/N)


def nSidedDie(p):
    n = len(p)
    cs = np.cumsum(p)
    cp = np.append(0, cs)
    r = np.random.rand()
    for k in range(0, n):
        if r > cp[k] and r <= cp[k + 1]:
            d = k + 1
    return d

def press_enter():
    input('Press enter to continue')

def main():
    N = 100000
    errorTransmission(N)
    press_enter()
    conditionalProbability(N)
    press_enter()
    conditionalProbability2(N)
    press_enter()
    enhancedTransmission(N)
main()