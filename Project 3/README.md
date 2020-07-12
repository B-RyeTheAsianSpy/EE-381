# Project 3 - Binomial and Poisson Distributions 
This project explores random experiments that can be described by probability distributions. These distributions are the Binomial and Poisson distributions.

Refer to the PDF report for full documentation of the project

## 1. Experimental Bernoulli Trials

This project will simulate the rolling of three multi-sided unfair dice n = 1,000 times. The probability vector for the multi-sided die is `p = [0.2, 0.1, 0.15, 0.3, 0.2, 0.05]`. A roll is considered a “success” if the first die rolls a “one,” the second die rolls a “two,” and the third die rolls a “three.” The experiment is repeated for `N = 10,000` times in order to generate a PMF plot.

## 2. Calculations Using Binomial Distribution

This experiment uses the theoretical formula for the Binomial Distribution to calculate the probabilities of successes for each roll of the unfair n-sided die in the previous experiment. The PMF plot is generated using the Binomial formula.

## 3. Approximation of Binomial by Poisson Distribution

In the event that the probability p of success in a Bernoulli trial is small and the number of trials n is large, we would use the Poisson distribution formula:

This approximation is only valid for rare events, i.e.:
- n > 50 – large number of trials
- 𝜆 = np < 5 – small probability of success

Using 𝜆 as a parameter and the formula, the experiment requires to plot the probability distribution function that approximates the distribution of the random variable

𝑋 = {𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑠𝑢𝑐𝑐𝑒𝑠𝑠𝑒𝑠 𝑖𝑛 𝑛 𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖 𝑡𝑟𝑖𝑎𝑙𝑠}