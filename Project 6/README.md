# Project 6 - Confidence Intervals

Refer to the PDF report for full documentation of the project

## 1. A Three-State Markov Chain

The following section focuses on three-state Markov chains. We are simulating three
different experiments:

- One single-simulation run for n = 15 steps
- One experiment with simulated probabilities for states R, N, S
- One experiment with probabilities obtained through the state transition matrix approach for states R, N, S

## 2. The Google PageRank Algorithm

This section is based on the PageRank algorithm, that is used in the Google search engine. The algorithm is used to rank the top websites from a user's search, and it is based on 
Markov chains.

In this experiment, we are simulating how the algorithm works in a web that consists of 5 pages.

## 3. Absorbing Markov Chains (Drunkard's Walk)

In this experiment, we are to simulate a "Drunkard's Walk," which is a Markov Chain that when a state reaches either state 0 or state (k - 1) (where k is the number of states), it will stay in that state for the remainder of the chain

## 4. Compute the Probability of Absorption Using the Simulated Chain

In this section, we are to calculate the probability of the chain ending in either state 0 or state 4. The probabilities for initial state in this simulation is `[0, 0, 1.0, 0, 0]`, which means the starting state will always be state 2. The simulation is run for N = 10,000 times.