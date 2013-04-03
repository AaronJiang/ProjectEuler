"""
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

This probelm bored, I wont waste time on it. So answers from 
http://blog.dreamshire.com/2009/03/26/project-euler-problem-41-solution/
Analysis

What is the value of n? We know it's between 4 and 9 
but that leaves a huge set of prime number candidates 
to search through. So let's eliminate some values of 
n by using the rule that any integer is divisible by 
3 or 9 whose sum of digits is divisible by 3 or 9; 
therefore composite and not prime.

9+8+7+6+5+4+3+2+1 = 45,
8+7+6+5+4+3+2+1 = 36,
6+5+4+3+2+1 = 21, and
5+4+3+2+1 = 15,
all of which are divisible by 3 and therefore could 
not yield a 1 to {5, 6, 8, 9} pandigital prime. So 
that leaves 4 and 7 digit prime numbers less than 
4321 and 7654321 respectively. Since we want the 
largest pandigital prime we'll check the 7 digit 
group first.

"""
from Helper import isPrime, isPandigital
 
n = 7654321
while not(isPrime(n) and isPandigital(n, 7)):
  n-=2
print "Answer to PE41 = ", n