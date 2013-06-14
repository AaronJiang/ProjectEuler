"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least
two positive integers?
"""

# the same solution to problem 31
target = 100
coins = range(1,100)
ways = [1]+[0]*target
 
for coin in coins:
	for i in range(coin, target+1):
		ways[i] += ways[i-coin]
 
print ways[target]
