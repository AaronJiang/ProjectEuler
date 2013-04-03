"""
The decimal number, 585 = 1001001001 (binary), 
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either 
base, may not include leading zeros.)

This probelm bored, I wont waste time on it. So answers from 
http://blog.dreamshire.com/2009/03/29/project-euler-problem-36-solution/
"""

from Helper import isPalidrome
dec2bin = lambda n: str(bin(n))[2:]
 
s = 0 
limit = 1000000
 
for n in range(1, limit, 2):
  if isPalidrome(n) and isPalidrome(dec2bin(n)):
    s += n
 
print "Answer to PE36 = ", s