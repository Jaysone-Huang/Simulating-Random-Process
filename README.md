# Simulating-Random-Process
Created a simulation that utilizes a Geometric sequence where you count the number of flips needed to get a head from a coin flip. Using that number of flips, you utilize the Bernoulli sequence and count the number of heads obtained.
 Suppose you have two coins for which
𝑃(Coin 1 = heads) = 𝑝,
and
𝑃(Coin 2 = heads) = 𝑞,
Flip Coin 1 until the first head appears, counting the number of flips. Let 𝑁 be the number of flips in
this first sequence. Next, perform 𝑁 flips of Coin 2, counting the number of heads. Let 𝑌 be the number
of heads in this second sequence. Note that 𝑁 is Geometric with parameter 𝑝. If 𝑋𝑖
is the random
variable
𝑋𝑖 = {
1 if the 𝑖
th flip of Coin 2 is heads
0 if the 𝑖
th flip of Coin 2 is tails
then we see each 𝑋𝑖
is Bernoulli with parameter 𝑞. We assume of course that all coin flips are
independent, so the set {𝑁, 𝑋1, 𝑋2, … } is independent. Observe that
𝑌 = 𝑋1 + 𝑋2 + ⋯ ⋯ ⋯ + 𝑋𝑁
is the sum of a random number of independent identically distributed (iid) random variables. We will
derive the mean and variance of 𝑌, in terms of 𝑝 and 𝑞, in lecture. Your goal in this assignment will be
to compute both 𝐸[𝑌] and 𝑉𝑎𝑟(𝑌) experimentally, for various values of 𝑝 and 𝑞. Each approximate
mean and variance you compute in this project will be obtained by performing 10,000 trials of the above
experiment.