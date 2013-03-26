from Helper import isPrime

primes = ''
for i in range(2, 10000):
	if isPrime(i):
		primes += str(i)+'\n'

f = open('primes.txt','w')
f.write(primes)
f.close()		