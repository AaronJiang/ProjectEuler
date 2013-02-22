"""
A Pythagorean triplet is a set of three natural numbers, 
a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which 
a + b + c = 1000.

Find the product abc.
"""

def pythagorean_loop():
	product = 0
	for c in range(1, 1000):
		for b in range(1, c):
			for a in range(1, b):
				if (a*a + b*b == c*c) and (a + b + c == 1000):
					product = a * b * c
					return product # I dont know how to break mutiply loops

print pythagorean_loop()