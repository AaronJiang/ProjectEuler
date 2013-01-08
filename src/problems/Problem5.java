/**
 * Problem 5
 * 
 * 2520 is the smallest number that can be divided 
 * by each of the numbers from 1 to 10 without any 
 * remainder. What is the smallest positive number 
 * that is evenly divisible by all of the numbers 
 * from 1 to 20?
 * http://projecteuler.net/problem=5
 * 
 * @author Aaron Jiang 2013-01-08
 * 
 */
package problems;

public class Problem5 {

	public static void main(String[] args) {
		long lcd = 1L; //least common multiple
		
		for(int i=1; i<20; i++){
			lcd = LCD(lcd,i+1);
			System.out.println(lcd);
		}
		
	}
	
	//Get least common multiple
	public static long LCD(long a, long b) {
	   return a*b/GCD(a,b);
	}
		
	//Get greatest common divisor
	public static long GCD(long a, long b) {
	   if (b==0) return a;
	   return GCD(b,a%b);
	}
}
