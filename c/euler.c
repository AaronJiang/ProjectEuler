/**
* Euler functions, compile euler.c with problem***.c
*/
#include <math.h>

long fibonacci(long n) {
	return n <= 2 ? 1 : fibonacci(n-1) + fibonacci(n-2);
}

int isPrime(long n) {
	if (n < 2) return 0;

	int i = 2;
	while (i <= sqrt(n)) {
		if (n % i == 0) 
			return 0;
		i++;
	}
	return 1;
}

int isPalidrome(long orig)
{
	long reversed = 0, n = orig;
	while (n > 0) {
		reversed = reversed * 10 + n % 10;
		n /= 10;
	}

	return orig == reversed;
}
