"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five 
thousand different ways?
"""
# based on solution to problem 31
from Helper import isPrime

def computeWays(n):
	ways = [1]+[0]*n
	for p in primes:
		for i in range(p, n+1):
			ways[i] += ways[i-p]
	return ways[n]

def main():
	n = 3
	while True:
		if isPrime(n-1): primes.append(n-1)
		ways = computeWays(n)
		if ways > 5000:
			print n
			break
		n += 1

if __name__ == '__main__':
	global primes
	primes = []
	main()		
