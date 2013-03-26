from math import sqrt, pow

def fibonacci(n):
	if n<=2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def isPrime(n):
	for i in xrange(2, int(sqrt(n))+1):
		if n%i == 0:
			return False
	if n == 1 : return False		
	return True

def isPalidrome(n):
	return str(n)==str(n)[::-1]	

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

def isTruncatablePrime(n):
	number = str(n)
	length = len(number)
	flag = True
	for i in range(length):
		if (not isPrime(int(number[i:]))) or\
		(not isPrime(int(number[:length-i]))):
			flag = False
			break 

	return flag

def isConcatenated(n):
	for i in range(1,10):
		if n.count(str(i)) != 1:
			return False
	return True		

def isPandigital(n, s=9): 
	n=str(n);
	return len(n)==s and not '1234567890'[:s].strip(n)