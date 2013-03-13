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

# check if number have duplicated digits
def isIdenticalDigits(n):
	for digit in str(n):
		if str(n).count(digit) != 1:
			return False
	return True

n = 1000
sums = 0
while n < 98765:
	if isIdenticalDigits(n) == True:
		for i in range(2, int(sqrt(n))+1):
			if n % i == 0:
				numbers = str(i)+str(n/i)+str(n)
				if len(numbers) == 9 and isIdenticalDigits(numbers) == True \
				and numbers.count('0') == 0:
						sums += n
						break	
	n += 1
print sums
