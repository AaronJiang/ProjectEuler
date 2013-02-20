"""
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?
"""

from Helper import isPrime

i = 1
count = 0

while count <= 10001:
	if isPrime(i) == True:
		pnumber = i
		count += 1
	i += 1	

print pnumber	
