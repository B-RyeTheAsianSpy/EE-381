# Project 1: Random Numbers and Stochastic Experiments

Refer to the PDF report for full documentation of the project

## 1. Function for an n-sided Die
The experiment simulates a single roll of an n-sided die. In this case, we have 7-sided die for this experiment given by 

`p = [0.10,  0.15,  0,20,  0.05,  0.30, 0.10, 0.10]`

which is the probabilities for each side being rolled. All elements inside p must add up to “1.”  

## 2. Number of Rolls Needed to Get a “7” With Two Die 

The following experiment consists of rolling two die and keeping track of the number of rolls it will take until the summation of the faces is “7.” When the sum is a 7, the experiment is considered a “success” and will stop. The experiment is repeated `N = 100,000` times, and the program keeps track of the number of rolls it would take to get a sum of 7 each time. 

## 3. Getting 50 Heads When Tossing 100 Coins

The following experiment consists of tossing 100 coins and recording the number of “heads.” The experiment is considered a “success” when 50 heads are counted out of 100 tosses. The experiment is repeated for `N = 100,000` times and the total number of successes are counted. 

## 4. The Password Hacking Problem 

In this experiment, our computer system uses a 4-letter password for login. A hacker creates a list of m random 4-letter words in order to access our system; the value of m is 80,000. If the hacker’s list contains at least one word that matches our password, then the experiment is considered a success. There are three parts to this experiment: 

- The experiment is repeated for `N = 1000 times` 

- The hacker creates a longer list of k*m letter words and the experiment is repeated for `N = 1000 times`. The value of k is 7.

- The previous experiment is repeated to find the approximate number `m` of words that must be contained in the list so that the probability of finding at least one of the words is `p = 0.5 `