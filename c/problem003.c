/**
*The prime factors of 13195 are 5, 7, 13 and 29.
*What is the largest prime factor of the number 600851475143 ?
* NEED TO COMPILE USING -lm in linux gcc
*/

#include <stdio.h>
#include "euler.h"
int main() 
{
	long long number = 600851475143LL, lanum = 0;
	int factor = 0, i = 2;

	while (i <= number) {
		if (number % i == 0) {
			if (isPrime(number / i)) {
				lanum = number / i;
				break;
			}
		}
		i++;
	}
	printf("largest num is %lld\n", lanum);
	return 0;
}