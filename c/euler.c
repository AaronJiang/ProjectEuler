/**
* Euler functions, compile euler.c with problem***.c
*/
#include <math.h>

int fibonacci(int n) {
	return n <= 2 ? 1 : fibonacci(n-1) + fibonacci(n-2);
}

int isPrime(int n) {
	if (n < 2) return 0;

	int i = 2;
	while (i <= sqrt(n)) {
		if (n % i == 0) 
			return 0;
		i++;
	}
	return 1;
}