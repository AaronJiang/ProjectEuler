/**
 * Problem 10
 * 
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 * Find the sum of all the primes below two million.
 * 
 * http://projecteuler.net/problem=10
 * 
 * @author Aaron Jiang 2013-02-01
 * 
 */
package problems;

public class Problem10 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {

		long sum = 0;
		
		for(long i=2; i<2000000; i++){
			if(isPrime(i)==true){
				sum += i;
			}
		}
		System.out.println(sum);
	}
	
	/**
	 * Check if number is prime
	 */
	public static boolean isPrime(long number){
		for(long i=2; i<=Math.sqrt(number); i++){
			if(number%i==0){
				return false;
			}
		}
		return true;
	}
}
