package baekjoon.step;

import java.util.Arrays;
import java.util.Scanner;

public class 숫자의개수2577 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] digits = new int[10];
		int multi = 1;

		for (int i = 0; i < 3; i++) 
			multi *= sc.nextInt();

		for (char c : String.valueOf(multi).toCharArray()) 
			digits[c - '0']++;
		
		Arrays.stream(digits).forEach(System.out::println);
	}
}