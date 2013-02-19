"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from Helper import isPrime

number = 600851475143
factor = 0

for i in xrange(2, number+1):
	if number%i == 0:
		if isPrime(number/i) == True:
			print number/i
			break
			
		
