"""
http://projecteuler.net/problem=15
Starting in the top left corner of a 2*2 grid, and only 
being able to move to the right and down, there are exactly 
6 routes to the bottom right corner.

How many such routes are there through a 20*20 grid?
"""
# directory contains the number of paths to 20*20 grid point
global pathList 
pathList = {}

def path_count(pos):
	""""
	return the number of paths to given position

	for example the number of paths to point (2,3) equals the 
	number of paths to (1,3) PLUS the number of paths to (2,2)
	"""

	#check if count already calculated
	if pos in pathList:
		return pathList[pos]

	else:
		# stop when return to start point
		if pos[0] == 1 and pos[1] == 1:
			count = 1
		else:
			# point in middle 
			if pos[0] != 1 and pos[1] != 1:
				# point on the diagonal
				count = path_count((pos[0]-1, pos[1])) + path_count((pos[0], pos[1]-1))
			# point on the border	
			elif pos[0] ==1 and pos[1] != 1:
				count = path_count((pos[0], pos[1]-1))	 
			elif pos[0] !=1 and pos[1] == 1:
				count = path_count((pos[0]-1, pos[1]))	

		# path number to (2,3) equals path number to (3,2)		
		pathList[pos] = count
		pathList[(pos[1],pos[0])] = count		
		return count	

print path_count((21,21))	
