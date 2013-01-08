/**
 * Problem 4
 * 
 * A palindromic number reads the same both ways. 
 * The largest palindrome made from the product of 
 * two 2-digit numbers is 9009 = 91 × 99. Find the 
 * largest palindrome made from the product of two 
 * 3-digit numbers.
 * http://projecteuler.net/problem=4
 * 
 * @author Aaron Jiang 2013-01-08
 * 
 */
package problems;

public class Problem4 {

	public static void main(String[] args) {
		int max = 0; //maximum palindrome
		int product = 0;
		
		//Check products from 100 to 999
		for(int i=100; i<=999; i++){
			for(int j=100; j<=999; j++){
				product = i*j;
				if(palindrome(product) && product>max){
					max = product;
				}
			}
		}
		System.out.print(max);
	}
	
	public static boolean palindrome(int number){
        int reversedNumber = 0;
        int originalNumber = number;
        int temp = 0;
        while(number > 0){
			//use modulus operator to strip off the last digit
		    temp = number%10;
			   
			//create the reversed number
			reversedNumber = reversedNumber * 10 + temp;
			number = number/10;
        }
        
        if(reversedNumber == originalNumber){
        	return true;
        }else{
        	return false;
        }
	}
}
