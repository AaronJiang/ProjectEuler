"""
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions 
with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit 
recurring cycle. It can be seen that 1/7 has a 
6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains 
the longest recurring cycle in its decimal fraction part.
"""
# Check the recurring of 1/n
# 1/n must be a rational number
def checkRecurring(n):
	numerator = 1
	denominator = n
	fractions = []
	
	i = 1
	while 1:
		numerator = numerator * 10 
		fractions.append( numerator / n )
		numerator = numerator % n
		if numerator == 0: 
			return 0
		else:	
			length = recurringLength(fractions)
			if length != False:
				return length
		i += 1

def recurringLength(numbers):
	for start in range(0, len(numbers)):
		for length in range(1, len(numbers[start:])/2+1):
			if numbers[start:start+length] == numbers[start+length: start+length+length]:
				if sum(numbers[start:start+length]) != 0:
					return len(numbers[start:start+length])
					break
	return False	

maxlength = 0
pointer = 2
# for i in range(2, 1000):
# 	length = checkRecurring(i)
# 	print length,
# 	if maxlength < length:
# 		maxlength = length
# 		pointer = i
print recurringLength([0,0,3,0,0,3])
# print maxlength
# print pointer