"""

It is possible to show that the square root of two 
can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, 
but the eighth expansion, 1393/985, is the first example 
where the number of digits in the numerator exceeds the 
number of digits in the denominator.

In the first one-thousand expansions, how many fractions 
contain a numerator with more digits than denominator?

"""
import sys 
sys.setrecursionlimit(2000) #1000 by default

def sqrtFraction(n):
	if n == 1:
		return [3, 2]
	else:
		prev = sqrtFraction(n-1)
		return [prev[0] + 2*prev[1], prev[0] + prev[1]]

count = 0
for i in range(1, 1001):
	fraction = sqrtFraction(i)
	if len(str(fraction[0])) > len(str(fraction[1])):
		count += 1
print count	
