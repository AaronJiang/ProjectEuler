/**
 * Problem 7
 * 
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, 
 * and 13, we can see that the 6th prime is 13.
 * What is the 10 001st prime number?
 * http://projecteuler.net/problem=7
 * 
 * @author Aaron Jiang 2013-01-30
 * 
 */
package problems;

public class Problem7 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int count = 0;
		long num = 2;
		while(count<10001){
			if(Problem7.isPrime(num)==true){
				count++;
			}
			num++;
		}
		System.out.println(--num);
		
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
