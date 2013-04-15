"""

It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
"""
from Helper import isPerm

n = 1
while True:
	flag = True
	for i in range(2, 7):
		if not isPerm(n, i*n):
			flag = False
			break

	if flag == True:
		print n
		break
	n += 1