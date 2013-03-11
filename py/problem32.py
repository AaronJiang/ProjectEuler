"""
We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once; for example, the 
5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 
9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be 
sure to only include it once in your sum.
"""
from math import sqrt

n = 1000
sums = 0
while n < 987654:
	for i in range(2, int(sqrt(n))+1):
		if n % i == 0:
			numbers = str(i)+str(n/i)+str(n)
			if len(numbers) != 9:
				break
			else:	
				flag = True
				for j in range(1,10):
					if numbers.count(str(j)) != 1:
						flag = False
						break

				if flag == True:
					sums += n
					print n
					break		
	n += 1
print sums