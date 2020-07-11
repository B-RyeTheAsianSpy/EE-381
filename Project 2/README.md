# Project 2 - Conditional Probabilities

This project explores the concept of conditional probabilities. The scenario for this is communication through a noisy channel

Refer to the PDF report for full documentation of the project

## 1. Probability of an Erroneous Transmission 

This project deals with message transmissions through a noisy communication channel. A digital message “M” is sent through the channel; its signal “S” consists of zeroes and ones.

- Symbol “0” appears in the signal with probability `p0 = 0.6`
- Symbol “1” appears in the signal with probability `1 - p0 = 0.4`

 Due to the noise in the channel, the bits may change, resulting in erroneous transmissions.

- A transmitted bit 0 may be received as 1 with probability `e0 = 0.05`
- A transmitted bit 1 may be received as 0 with probability `e1 = 0.03`

For this problem, we are to transmit a one-bit message, compare it to its signal, and count the number of times the experiment fails. The experiment is repeated for `N = 100,000 times`.

![fig1](https://github.com/Brian-E-Nguyen/EE-381/blob/documentation-update/Project%202/Figure1.png?raw=true)

## 2. Conditional Probability P(R = 1 | S = 1)

For this experiment, we are to create and transmit a one-bit message S as before and calculate the conditional probability 

`P(R = 1 | S = 1)`

For all bits in which `S = 1, if R = 1`, then the experiment is considered a success. The experiment is repeated for `N = 100,000` times

## 3. Conditional Probability: P(S = 1 | R = 1)

For this experiment, we are to create and transmit a one-bit message S as before and calculate the conditional probability 

`P(S = 1 | R = 1)` 

For all bits in which `R = 1`, if `S = 1`, then the experiment is considered a success. The experiment is repeated for `N = 100,000` times.

## 4. Enhanced Transmission Method

In this experiment, the transmission is enhanced by sending the same bit “S” three times `(S S S)`. Since this is the case, the received message will be `(R R R)`. 

- The possible received bits are `(R1 R2 R3) = { (000), (001), (010), (011), (100), (101), (110), (111) }`
- By using the *voting and majority rule*, we decide what bit is originally transmitted
    - For example: if `(R1 R2 R3) = (110)`, then the majority bit is 1. 
    - Another example: if `(R1 R2 R3) = (010)`, then the majority bit is 0.

- If the sent bits are the same as the received majority bit, then the experiment is considered a success; otherwise, it is a failure
    - For example: if `S = (000)` and `R = (001)`, then the experiment is considered a success because the decoded bit is `D = 0; S = D`
    - Another example: if `S = (111)` and `R = (001)`, then the experiment is considered a failure because the decoded bit is `D = 0, S ≠ D`

The experiment requires to count the number of times the transmitted bit “S” was received and decoded incorrectly for `N = 100,000 times`
