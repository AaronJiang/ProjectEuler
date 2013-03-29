"""

Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 
649^2 - 13*180^2 = 1.

It can be assumed that there are no solutions in positive 
integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, 
we obtain the following:

3^2 - 2*2^2 = 1
2^2 - 3*1^2 = 1
9^2 - 5*4^2 = 1
5^2 - 6*2^2 = 1
8^2 - 7*3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, 
the largest x is obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for 
which the largest value of x is obtained.
"""
from Helper import isSquare
from math import sqrt
max_x2 = 0
min_D = 1000

for D in range(61, 62):
	if not isSquare(D):
		y = 1
		while True:
			x2 = 1 + D*y*y
			if isSquare(x2):
				if max_x2 < x2:
					max_x2 = x2
					min_D = D
				break
			y += 1
print min_D
print sqrt(max_x2)

# y = 2
# checked_D = []

# nonsquares = []
# for i in range(2, 1001):
# 	if not isSquare(i):
# 		nonsquares.append(i)
# print 'done non squares for D'

# while y > 0:
# 	nonChecked_D = list(set(nonsquares) - set(checked_D))
# 	for D in nonChecked_D:
# 		x2 = 1 + D*y*y
# 		if isSquare(x2):
# 			print D,',',len(checked_D)
# 			checked_D.append(D)
# 			continue
# 	if len(checked_D) == 800:
# 		break		
# 	y += 1

# print len(checked_D)	