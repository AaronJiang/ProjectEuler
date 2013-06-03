"""
It turns out that 12 cm is the smallest length of wire that 
can be bent to form an integer sided right angle triangle 
in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent 
to form an integer sided right angle triangle, and other lengths 
allow more than one solution to be found; for example, 
using 120 cm it is possible to form exactly three different 
integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of 
L <= 1,500,000 can exactly one integer sided right angle triangle be formed?
"""

# Generate pythagorean triple using 
# http://en.wikipedia.org/wiki/Pythagorean_triple
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2
#  m > n, and m+n is odd and gcd(n,m) = 1

from math import sqrt
from Helper import gcd

Limit = 1500000
mlimit = int(sqrt(Limit/2)) + 1  # a+b+c<Limit
# list to point how many times the same value
# a + b + c has been caculated
wires = [0] * Limit 
count = 0

for m in range (2, mlimit):
	for n in range(1, m):
		if (m + n) % 2 == 1 and gcd(m, n) == 1:
			a = m**2 - n ** 2
			b = 2 * m * n
			c = m**2 + n ** 2
			length = a + b + c
			while length < Limit:
				wires[length] += 1
				if wires[length] == 1: 
					count += 1
				elif wires[length] == 2: 
					count -= 1
				length += a + b + c 
print count
