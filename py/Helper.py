from math import sqrt, pow

def fibonacci(n):
	if n<=2:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def isPrime(n):
	for i in xrange(2, int(sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def isPalidrome(n):
	if reverseInt(n) == n:
		return True
	else:
		return False	

def reverseInt(n):
	return int(str(n)[::-1])

def gcd(a, b):
    """Return greatest common divisor."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b / gcd(a, b)

def factors(n):
	res = []
	for i in range(1, int(sqrt(n))+1):
		if n%i == 0:
			res.append(i)
			res.append(n/i)
	return res		

def CollatzChain(n):
	chain = []
	while True:
		
		chain.append(n)
		if n == 1:
			break

		if (n%2 == 0):
			n = n/2
		else:
			n = 3*n + 1	
	return len(chain)		

def properFactors(n):
	factors = []
	for i in range(1, int(n**0.5)+1):
		if n%i == 0:
			factors.append(i)
			if n/i != i and i !=1 :
				factors.append(n/i)
	return factors		
	
def charToValue(charest, charcase):
	if charcase == 'UPPERCASE':
		return ord(charest) - 64
	elif charcase == 'LOWCASE':
		return ord(charest) - 96		