"""

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""
from Helper import isPrime
limit = 1000000

primes = [i for i in range(2, limit) if isPrime(i)]
(countmax, primemax)  = (1, 2)

for i in range(len(primes)-1):
	if countmax*primes[i] > limit: continue
	sums = primes[i]
	count = 1
	for j in range(i+1, len(primes)):
		sums += primes[j]
		if j - i + 1 < countmax: continue
		if sums > limit: break
		if sums in primes: 
			count = j - i + 1
			sumtmp = sums

	if countmax < count : 
		countmax = count
		primemax = sumtmp
		print countmax, primemax
