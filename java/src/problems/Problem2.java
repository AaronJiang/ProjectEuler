/**
 * Problem 2
 * 
 * Each new term in the Fibonacci sequence is generated by
 * adding the previous two terms. By starting with 1 and 2, 
 * the first 10 terms will be:
 * 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 * By considering the terms in the Fibonacci sequence whose 
 * values do not exceed four million, find the sum of the 
 * even-valued terms.
 * http://projecteuler.net/problem=2
 * 
 * @author Aaron Jiang 2013-01-04
 * 
 */
package problems;

public class Problem2 {

	public static void main(String[] args) {
		int end = 4000000;
		int sum = 0;
		int n = 1; //the fibonacci set pointer
		int fib = fibNumber(n);
		while(fib<end){
			if(fib%2==0){
				//System.out.println(fib);
				sum += fib;
			}
			fib = fibNumber(++n);
			
		}
		System.out.println(sum);
	}
	
	/**
	 * Get Fibonacci number
	 * @param n the pointer
	 * @return the value of Fibonacci(n)
	 */
	public static int fibNumber(int n){
		if(n<=2){
			return n;
		}else{
			return fibNumber(n-1) + fibNumber(n-2);
		}
	}
}
