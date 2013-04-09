"""

The arithmetic sequence, 1487, 4817, 8147, in which each of 
the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from Helper import isPrime, isPerm

n = 1489 	# must be odd
while True:
	b, c = n+3330, n+6660
	if isPrime(n) and isPrime(b) and isPrime(c) \
	and isPerm(n,b) and isPerm(b,c): break
	n += 2
 
print str(n)+str(b)+str(c)