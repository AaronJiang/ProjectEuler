"""

In the card game poker, a hand consists of five cards and are ranked, 
from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of 
the highest value wins; for example, a pair of eights beats a pair 
of fives (see example 1 below). But if two ranks tie, for example, 
both players have a pair of queens, then highest cards in each hand 
are compared (see example 4 below); if the highest cards tie then 
the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD 	  2C 3S 8S 8D TD   	Player 2
		Pair of Fives 	  Pair of Eights 	
2	 	5D 8C 9S JS AC 	  2C 5C 7D 8S QH	Player 1	
		Highest card Ace  Highest card Queen
3	 	2D 9C AS AH AC 	  3D 6D 7D TD QD	Player 2
		Three Aces 		  Flush with Diamonds
4	 	4D 6S 9H QH QC	  3D 6D 7H QD QS    Player 1
		Pair of Queens    Pair of Queens
		Highest card Nine Highest card Seven
5	 	2H 2D 4C 4D 4S 	  3C 3D 3S 9S 9D
		Full House		  Full House  		Player 1
		With Three Fours  with Three Threes 
	 	
The file, poker.txt, contains one-thousand random hands dealt 
to two players. Each line of the file contains ten cards 
(separated by a single space): the first five are Player 1's 
cards and the last five are Player 2's cards. You can assume 
that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there 
is a clear winner.

How many hands does Player 1 win?
"""
global allcards 
allcards = range(2, 15)

# set card number and suit for each line
def setCards(cards):
	number = []
	for card in cards:
		n = card[:-1]
		if n == 'T': n = '10'
		elif n == 'J': n = '11'
		elif n == 'Q': n = '12'
		elif n == 'K': n = '13'
		elif n == 'A': n = '14'
		number.append(int(n))
	number.sort()
	suit = [i[-1] for i in cards]
	ordered = {'number':number, 'suit':suit}
	return ordered		

# return order card number for comparing values
# and move the matched numbers to last.
def isFlush(cards):
	suit = cards['suit']
	number = cards['number']
	if suit.count(suit[0]) == 5:
		return number	

def isStraight(cards):
	number = cards['number']
	idx = allcards.index(number[0])
	if number == allcards[idx:idx+5]:
		return number

def isRoyalFlush(cards):
	number = cards['number']
	if number == allcards[-5:] and isFlush(cards):
		return number	

def isStraightFlush(cards):
	number = cards['number']
	if isStraight(cards) and isFlush(cards):
		return number

def isFourKind(cards):
	number = cards['number']
	# move four kind cards to last
	if number.count(number[0]) == 4:
		number.insert(0, number.pop(-1)) 
		return number
	elif number.count(number[-1]) == 4:
		return number		

def isFullHouse(cards):
	number = cards['number']
	if number.count(number[0]) == 2 and number.count(number[-1]) == 3:
		return number
	elif number.count(number[0]) == 3 and number.count(number[-1]) == 2:
		number = number[-2:] + number[:3]
		return number

def isThreeKind(cards):
	number = cards['number']
	if number.count(number[0]) == 3: 
		number = number[-2:] + number[:3]
		return number
	elif number.count(number[1]) == 3:
		number.insert(1, number.pop(-1))
		return number
	elif number.count(number[2]) == 3:
		return number	

def isTwoPairs(cards):
	count = 0
	number = cards['number']
	for i in number:
		if number.count(i) == 1:
			count += 1
	if count == 1:		
		number.insert(0, number.pop(number.index(i)))
	if number[1] == number[2] and number[3] == number[4]:
		return number	

def isOnePair(cards):
	number = cards['number']
	count = 0
	length = len(number)
	for i in range(length-1):
		if number[i] == number[i+1]:
			count += 1
			idx = i
	if count == 1:
		number.insert(length, number.pop(idx+1))
		number.insert(length-1, number.pop(idx))
		return number

def isHighCard(cards):
	return cards['number']

def compareTwoPlayer(p1, p2):
	(p1_index, p2_index) = (9, 9)
	# funs = [isRoyalFlush, isStraightFlush, isFourKind, isFullHouse, \
	# isFlush, isStraight, isThreeKind, isTwoPairs, isOnePair, isHighCard]
	funs = [isRoyalFlush, isStraightFlush, isFourKind, isFullHouse, \
	isFlush, isStraight, isThreeKind, isTwoPairs, isOnePair, isHighCard]

	for i in range(len(funs)):
		p1_number = funs[i](p1)
		if p1_number:
			p1_index = i
			break

	for i in range(len(funs)):
		p2_number = funs[i](p2)
		if funs[i](p2):
			p2_index = i
			break

	# print p1_index, p2_index
	# print p1_number, p2_number
	# compare special cards
	if p1_index < p2_index: 
	 	return True

	# compare special cards, if sepcial cards equal
	# compare other cards from highest to lowest
	elif p1_index == p2_index:
		for i in range(4, -1, -1):
			if p1_number[i] > p2_number[i]:
				return True
			elif p1_number[i] < p2_number[i]:
				return False
		return False # tie	
	else:
		return False			

count = 0
f = open('poker.txt', 'r')
for line in f:
	line = line.strip("\n")
	cards = line.split(" ")
	p1 = setCards(cards[:5])
	p2 = setCards(cards[5:])
	if compareTwoPlayer(p1, p2):
		count += 1
print count		

# cards = setCards(['AD', 'KD', 'JD', 'QD', 'TD'])
# print isRoyalFlush(cards) 
