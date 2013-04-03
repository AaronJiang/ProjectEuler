"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	Pn=n(3n-1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	Hn=n(2n-1) 	  	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal
"""
from Helper import isPentagonal, isHexagonal

n = 286

while True:
	tn = n*(n+1)/2
	if isPentagonal(tn) and isHexagonal(tn):
		print tn
		break
	n += 1	