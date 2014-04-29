/**
*2520 is the smallest number that can be divided 
*by each of the numbers from 1 to 10 without 
*any remainder.
*
*What is the smallest positive number that is evenly 
*divisible by all of the numbers from 1 to 20?
*/
#include <stdio.h>

void main() 
{
	long lnum = 1;
	int i;
	for (i = 1; i <= 20; i++) {
		lnum = lcm(lnum, i);
	}
	printf("%ld\n", lnum);
}