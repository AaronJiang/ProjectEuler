"""
n! means n * (n-1) * ... * 3 * 2 * 1
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

products = 1
for i in range(1, 100+1):
	products *= i

sums = 0
products = str(products)
for i in products:
	sums += int(i)

print sums	