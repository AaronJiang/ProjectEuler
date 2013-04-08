"""

The arithmetic sequence, 1487, 4817, 8147, in which each of 
the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from Helper import isPrime
from itertools import permutations

def permutations(n):
	return permutations(n)

# for i in range(1001, 4999):
# 	if isPrime(i):

print permutations(range(1,3))