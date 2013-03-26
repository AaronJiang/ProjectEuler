"""

An irrational decimal fraction is created by concatenating
the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find 
the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
This probelm bored, I wont waste time on it. So answers from 
http://blog.dreamshire.com/2009/05/25/project-euler-problem-40-solution/
"""

n, c = 0, '.'
while (len(c)<=1000000):
	n+=1
	c+=str(n)
print "Answer to PE40 =", int(c[100])*int(c[1000])*int(c[10000])*int(c[100000])*int(c[1000000])