"""
You are given the following information, but you may 
prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, 
    but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during 
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# Return of many days of a given month
def monthdays(month, year):
	monthin31 = [1,3,5,7,8,10,12]
	monthin30 = [4,6,9,11]
	if month in monthin31:
		return 31
	elif month in monthin30:
		return 30
	else:
		if (year%4 == 0 and year%100 != 0) or year%400 == 0:
			return 29
		else:
			return 28			

# Return the next first day of given month
# 0 equals sunday, 1 equals monday
def nextFirstday(currentFirstday, currentmonthdays):
	return (currentFirstday + currentmonthdays%7) % 7

# Get first day of Jan 1901
firstday = 1
for year in range(1900, 1901):
	for month in range(1,13):
		monthday = monthdays(month, year)
		firstday = nextFirstday(firstday, monthday)

# Calculate sundays on first day of month
sundays = 0
for year in range(1901, 2001):
	for month in range(1,13):
		monthday = monthdays(month, year)
		if firstday == 0:
			sundays += 1
		firstday = nextFirstday(firstday, monthday)
		
print sundays
