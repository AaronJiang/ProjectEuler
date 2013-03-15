"""

The fraction 49/98 is a curious fraction, as an inexperienced 
mathematician in attempting to simplify it may incorrectly 
believe that 49/98 = 4/8, which is correct, is obtained by 
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator 
and denominator.

If the product of these four fractions is given in its lowest common 
terms, find the value of the denominator.

This probelm bored, I wont waste time on it. So answers from 
http://blog.dreamshire.com/2009/04/22/project-euler-problem-33-solution/
"""
d = 1
for i in range(1, 10):
  for j in range(1, i):
    for k in range(1, j):
      ki = k*10 + i
      ij = float(i)*10 + j
      if (k*ij == ki*j):
        d *= ij/ki
print "Answer to PE33 = ",d