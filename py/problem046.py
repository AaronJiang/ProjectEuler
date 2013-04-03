"""

It was proposed by Christian Goldbach that every odd 
composite number can be written as the sum of a prime 
and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written 
as the sum of a prime and twice a square?
"""
from Helper import isPrime, isSquare

primes = [2]
n = 3

while True:
	if n % 2 == 1 and isPrime(n) == False:
		flag = False
		for i in primes:
			if isSquare((n-i)/2):
				flag = True
				break
		if flag == False:
			print n
			break
	if isPrime(n):
		primes.append(n) 

	n += 1