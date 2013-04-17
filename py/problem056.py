"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, 
what is the maximum digital sum?
"""

def sumDigits(n):
	n = str(n)
	sum = 0
	for i in n:
		sum += int(i)
	return sum

max = 0
for a in range(1, 100):
	for b in range(1, 100):
		sum = sumDigits(a**b)
		if sum > max:
			max = sum

print max		