package unl.cse;

import java.util.Scanner;

/**
 * A demonstration/driver program that interactively
 * reads input from the user (command line) and computes
 * various statistics on the entered values.
 * 
 * @author cbourke
 *
 */
public class StatisticsDemo {

	public static void main(String args[]) {
		
		Scanner s = new Scanner(System.in);
		
		int[] array = new int[args.length];
		
		for (int i = 0; i < args.length; i++) {
			array[i] = Integer.parseInt(args[i]);
		}
		
		int min = Statistics.getMin(array);
		int max = Statistics.getMax(array);
		int sum = Statistics.getSum(array);
		double ave = Statistics.getAverage(array);
		
		System.out.println("The sum is " + sum);
		System.out.println("The average is " + ave);
		System.out.println("The highest is " + max);
		System.out.println("The lowest is " + min);

	}
}
