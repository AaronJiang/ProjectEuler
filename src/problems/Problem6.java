/**
 * Problem 6
 * 
 * The sum of the squares of the first ten natural numbers is,
 * 12 + 22 + ... + 102 = 385
 * The square of the sum of the first ten natural numbers is,
 * (1 + 2 + ... + 10)2 = 552 = 3025
 * Hence the difference between the sum of the squares of the 
 * first ten natural numbers and the square of the sum is 
 * 3025 − 385 = 2640.
 * 
 * Find the difference between the sum of the squares of the 
 * first one hundred natural numbers and the square of the sum.
 * 
 * http://projecteuler.net/problem=6
 * 
 * @author Aaron Jiang 2013-01-09
 * 
 */
package problems;

public class Problem6 {

	public static void main(String[] args) {
//		for(int i=1; i<=100; i++){
//			sumsquare += i;
//		}
//		sumsquare = (int)Math.pow(sumsquare,2);
//		
//		for(int i=1; i<=100; i++){
//			squaresum += (int)Math.pow(i,2);
//		}
		
		
		//((1 + 2 + ... + n)^2 = n^2 * (n+1)^2 * 1/4
		int n = 100;
		int sumsquare = n*n*(n+1)*(n+1)/4;
		
		//1^2 + 2^2 + ... + n^2 = n * (n+1) * (2n+1) * 1/6
		int squaresum = n*(n+1)*(2*n+1)/6;
		
		System.out.println(sumsquare-squaresum);
	}

}
