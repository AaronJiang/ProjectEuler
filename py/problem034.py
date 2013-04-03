"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the 
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

This probelm bored, I wont waste time on it. So answers from 
http://blog.dreamshire.com/2009/04/22/project-euler-problem-33-solution/
"""

#If n is a natural number of d digits that is a factorion, 
#then 10d - 1 <= n <= 9!d and this fails to hold for d >= 8. 
#Thus n has 7 digits and the maximum sum of factorials of 
#digits for a 7 digit number is 9!7 = 2,540,160, 
#which is the upper bound.
fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
s = 0
 
for n in range(10, 50000):
  x = sum( fact[int(d)] for d in str(n) )
  if n == x: s+=n
 
print "Answer to PE34 = ",s