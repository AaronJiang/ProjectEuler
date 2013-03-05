"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the 
digits 1, 2, 3 and 4. If all of the permutations are 
listed numerically or alphabetically, we call it 
lexicographic order. 

The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of 
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
# numbers = []
# positions = {}

# def availableDigits(excludedDigits, index):
# 	digits = range(10)
# 	for i in range(index):
# 		digits.remove(excludedDigits[i])

# 	return digits	

# for pos0 in range(10):
# 	positions = {}
# 	positions[0] = pos0
# 	for pos1 in availableDigits(positions, 1):
# 		positions[1] = pos1
# 		for pos2 in availableDigits(positions, 2):
# 			positions[2] = pos2
# 			for pos3 in availableDigits(positions, 3):
# 				positions[3] = pos3
# 				for pos4 in availableDigits(positions, 4):
# 					positions[4] = pos4
# 					for pos5 in availableDigits(positions, 5):
# 						positions[5] = pos5
# 						for pos6 in availableDigits(positions, 6):
# 							positions[6] = pos6
# 							for pos7 in availableDigits(positions, 7):
# 								positions[7] = pos7
# 								for pos8 in availableDigits(positions, 8):
# 									positions[8] = pos8
# 									for pos9 in availableDigits(positions, 9):
# 										positions[9] = pos9
# 										numbers.append( int( str(pos0)+str(pos1)+str(pos2) + str(pos3)+str(pos4)+str(pos5)+str(pos6)+str(pos7)+str(pos8)+str(pos9)) )


# sorted(numbers)
# print numbers[999999]


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = []
 
for j in range(999999):
 
    for k in range(len(a) - 1):
        if a[k] < a[k+1]:
            largest_k = k
 
    for l in range(len(a)):
        if a[largest_k] < a[l]:
            largest_l = l
 
    temp = a[:]
    a[largest_l] = temp[largest_k]
    a[largest_k] = temp[largest_l]
    temp = a[:]
 
    for i in range((len(a)-1) - (largest_k + 1)):
        a[largest_k + 1 + i] = temp[len(a) - 1 - i]
        a[len(a) - 1 - i] = temp[largest_k + 1 + i]
 
print(a)