"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from Helper import isPrime


top = 2000000
sum = 0

for i in range(2, top):
	if isPrime(i) == True:
		sum += i
print sum		
