"""
This problem has so many mathematical symbol, please view at
http://projecteuler.net/problem=53
"""
from Helper import combinator

limit = 1000000

count = 0
for n in range(1, 101):
	for r in range(2, n):
		if combinator(n, r) > limit:
			count += 1

print count			 