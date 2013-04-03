"""
Surprisingly there are only three numbers that can be written 
as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum 
of fifth powers of their digits.

"""

n = 10
sums = 0

while True:
	numbers = str(n)

	# break if max sum is less than n
	if n > 9**5*len(numbers):
		break

	pows = 0	
	for i in numbers:
		pows += int(i)**5

	if n == pows:
		sums += n
	n += 1
print sums