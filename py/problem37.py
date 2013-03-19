"""
The number 3797 has an interesting property. 
Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime 
at each stage: 3797, 797, 97, and 7. Similarly we 
can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are 
both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be 
truncatable primes.
"""
from Helper import isTruncatablePrime, isPrime

# n = 11
# sums = 0
# count = 0

# while True:
# 	flag = True
# 	for i in (0,4,6,8):
# 		if str(n).count(str(i)) > 0:
# 			flag = False
# 			break

# 	if flag == True and isPrime(n) == True:		
# 		if isTruncatablePrime(n):
# 			print n
# 			count += 1
# 			sums += n
# 			if count == 11:
# 				break

# 	n += 2
# print sums	

print isPrime(23339)