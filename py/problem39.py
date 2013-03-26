"""
If p is the perimeter of a right angle triangle with integral 
length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

This probelm bored, I wont waste time on it. So answers from 
http://blog.dreamshire.com/2009/04/22/project-euler-problem-39-solution/
"""
t_max = 0
p_limit = 1000
 
for p in range(p_limit//2, p_limit+1, 2):
  t = 0;
  for a in range(2, p/4+1):
    if  p*(p - 2*a) % (2*(p-a)) == 0: t += 1
    if t > t_max: (t_max, p_max) = (t, p)
 
print "Answer to PE30 = ", p_max