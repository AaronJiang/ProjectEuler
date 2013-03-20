from Helper import isPrime
primes = []
for i in range(2, 10000):
	if isPrime(i):
		primes.append(i)
L = len(primes)
		
px = dict()
pi = 1
for pi in range(1,L):
  p=primes[pi]
  if p==5: continue
  px[p]=set()
  for qi in range(pi,L):
    q=primes[qi]
    if isPrime(int(str(p) + str(q))) and isPrime(int(str(q) + str(p))):
      px[p].add(q)
 
for xx in px:
  for axx in px[xx]:
    set_a = px[xx] & px[axx]
    if len(set_a)>0:
      for bxx in set_a:
        set_b = set_a & px[bxx]
	if len(set_b)>0:
	  for cxx in set_b:
	    set_c = set_b & px[cxx]
	    if len(set_c)>0: print xx, axx, bxx, cxx, set_c