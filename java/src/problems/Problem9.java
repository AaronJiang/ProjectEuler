/**
 * Problem 9
 * 
 * A Pythagorean triplet is a set of three natural numbers, 
 * a < b < c, for which, a^2 + b^2 = c^2 
 * For example, 32 + 42 = 9 + 16 = 25 = 52.
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 * 
 * http://projecteuler.net/problem=9
 * 
 * @author Aaron Jiang 2013-02-01
 * 
 */
package problems;

public class Problem9 {
	public static void main(String args[]){
		for(int c=3; c<=997; c++){
			for(int b=2; b<c; b++){
				for(int a=1; a<b; a++){
					if( (a+b+c)==1000 && (a*a+b*b)==(c*c) ){
						System.out.println("Find matched numbers:"+a+","+b+","+c);
						System.out.println("The product of three numbers is:"+a*b*c);
					}
				}
			}
		}
	}
}
