from math import sqrt

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
