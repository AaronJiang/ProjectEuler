"""
Each new term in the Fibonacci sequence is 
generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms 
will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci 
sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
from Helper import fibonacci

sum = 0
n = 1
fnum = fibonacci(n)

while fnum <= 4000000:
	if fnum%2 == 0:
		sum += fnum
	n += 1
	fnum = fibonacci(n)

print sum
