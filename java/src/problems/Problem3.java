/**
 * Problem 3
 * 
 * The prime factors of 13195 are 5, 7, 13 and 29. 
 * What is the largest prime factor of the number 600851475143 ?
 * http://projecteuler.net/problem=3
 * 
 * @author Aaron Jiang 2013-01-04
 * 
 */
package problems;

public class Problem3 {

	public static void main(String[] args) {
		long number = 600851475143L;
		for(long i=2; i<number; i++){
			/*
			 * If i is the first factor of this number, (number/i) must
			 * be biggest factor of this number. And remember to check
			 * if (number/i) is prime or not.
			 */
			if(number%i==0){
				if(isPrime(number/i)==true){
					System.out.println(number/i);
					break;
				}
			}
		}

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
