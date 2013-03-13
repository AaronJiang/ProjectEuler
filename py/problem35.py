"""
The number, 197, is called a circular prime because 
all rotations of the digits: 197, 971, and 719, are 
themselves prime.

There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from Helper import isPrime

count = 1
n = 3
while n < 1000000:
	if isPrime(n):
		digits = str(n)

		flag = True
		for i in range(len(digits)):
			digits = digits[1:] + digits[0]
			if isPrime(int(digits)) == False:
				flag = False
				break
		if flag == True:
			count += 1		
	n += 2 # step over even number 	

print count