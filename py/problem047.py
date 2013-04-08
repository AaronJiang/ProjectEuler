"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.
Find the first four consecutive integers to have four distinct prime factors. 
What is the first of these numbers?

"""

from Helper import factors, isPrime

def primeCount(x):
	count = 0
	for i in x:
		if isPrime(i):
			count += 1
	return count
	
n = 1	
while True:
	if primeCount(factors(n)) == 4 and primeCount(factors(n+1)) == 4 \
	and primeCount(factors(n+2)) == 4 and primeCount(factors(n+3)) == 4:
		print n
		break
	n += 1