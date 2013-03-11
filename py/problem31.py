"""
In England the currency is made up of pound, L, 
and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).

It is possible to make L2 in the following way:

    1*L1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can L2 be made using any number of coins?
"""
target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [1]+[0]*target
 
for coin in coins:
  for i in range(coin, target+1):
    ways[i] += ways[i-coin]
 
print "Answer to PE31 = ", ways[target]
