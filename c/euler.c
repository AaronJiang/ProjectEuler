/**
* Euler functions, compile euler.c with problem***.c
*/
int fibonacci(int n) {
	return n <= 2 ? 1 : fibonacci(n-1) + fibonacci(n-2);
}