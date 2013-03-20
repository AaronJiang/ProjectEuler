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

# find primes under 100000
primes = []
for i in range(2, 10000):
	if isPrime(i):
		primes.append(i)
primes.remove(2)
primes.remove(5)
print 'finished 10000 primes'		

#check if a list of combined primes still prime
# only need to compare the last number with 
# the numbers before in interation 
def combinePrime(lists):
	for i in lists[:-1]:
		if isPrime(int(str(i)+str(lists[-1]))) == False or \
		isPrime(int(str(lists[-1])+str(i))) == False :
			return False
	return True

sums = 10000000
for i in primes[:-4]:
	for j in primes[primes.index(i)+1:-3]: 
		if combinePrime([i, j]):
			for k in primes[primes.index(j)+1:-2]: 
				if combinePrime([i, j, k]):
					for l in primes[primes.index(k)+1:-1]: 
						if combinePrime([i, j, k, l]):
							for m in primes[primes.index(l)+1:]: 
								if combinePrime([i, j, k, l, m]):
									sums_new = i + j + k + l + m
									print [i, j, k, l, m]
									if sums_new < sums:
										sums = sums_new
print sums											

# length = len(primes)

# for i in range(length):
# 	for j in range(i+1, length):
# 		if combinePrime([primes[i], primes[j]]):
# 			for k in range(j+1, length):
# 				if combinePrime([primes[i], primes[j], primes[k]]):
# 					for l in range(k+1, length):
# 						if combinePrime([primes[i], primes[j], primes[k], primes[l]]):
# 							for m in range(l+1, length):
# 								if combinePrime([primes[i], primes[j], primes[k], primes[l], primes[m]]):
# 									print primes[i], primes[j], primes[k], primes[l], primes[m]
