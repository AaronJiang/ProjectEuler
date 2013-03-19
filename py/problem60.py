"""

The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in 
any order the result will always be prime. 

For example, taking 7 and 109, both 7109 and 1097 
are prime. The sum of these four primes, 792, represents
 the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which 
any two primes concatenate to produce another prime.
"""
from Helper import isPrime
import sys

# find primes under 100000
global primes
primes = []
for i in range(2, 99999):
	if isPrime(i):
		primes.append(i)


#check if a list of combined primes still prime 
def combinePrime(lists):
	# only need to compare the last number with 
	# the numbers before in interation
	for i in lists[:-1]:
		if int(str(i)+str(lists[-1])) not in primes or \
		int(str(lists[-1])+str(i)) not in primes:
			return False
	return True

length = len(primes)
for i in primes:
	for j in primes[primes.index(i)+1:]: 
		if combinePrime([i, j]) == False:
			continue
		for k in primes[primes.index(j)+1:]: 
			if combinePrime([i, j, k]) == False:
				continue		
			for l in primes[primes.index(k)+1:]: 
				if combinePrime([i, j, k, l]) == False:
					continue
				else:
					print [i, j, k, l]	
					sys.exit()	
				# for m in primes[primes.index(l)+1:]: 
				# 	if combinePrime([i, j, k, l, m]) == False:
				# 		continue
				# 	else:
				# 		print [i, j, k, l, m]	 		