/**
*A palindromic number reads the same both ways. 
*The largest palindrome made from the product 
*of two 2-digit numbers is 9009 = 91 * 99.
*
*Find the largest palindrome made from the 
*product of two 3-digit numbers.
*/
#include <stdio.h>

void main ()
{
	long product = 0, i, j, number;

	for (i = 100; i < 1000; i++) {
		for (j = 100; j < 1000; j++) {
			number = i * j;
			if (isPalidrome(number) == 1) {
				if (product < number) {
					product = number;
				}
			}
		}
	}
	printf("largest product is %ld\n", product);
}
