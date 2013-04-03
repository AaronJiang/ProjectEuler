"""

The nth term of the sequence of triangle numbers 
is given by, tn = (1/2)n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding 
to its alphabetical position and adding these values we form 
a word value. For example, the word value for SKY is 
19 + 11 + 25 = 55 = t10. 

If the word value is a triangle number then we shall call 
the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), 
a 16K text file containing nearly two-thousand common English 
words, how many are triangle words?
"""
from Helper import charToValue
from math import sqrt, floor

def wordValue(word):
	sums = 0
	for char in word:
		sums += charToValue(char, 'UPPERCASE')
	return sums

f = open('words.txt', 'r')
words = f.read().split(',')

count = 0
for word in words:
	word = word.strip('"')
	num = wordValue(word)
	# if n is the solution, n<=sqrt(2*num)<=n+1
	n = floor(sqrt(2*num))
	if num == n*(n+1)/2:
		count += 1

print count