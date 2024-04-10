package baekjoon.step;

import java.util.Arrays;
import java.util.Scanner;

public class 평균은넘겠지4344 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();	

		for (int i = 0; i < n; i++) {
			int student = sc.nextInt();
			int[] arr = new int[student];

			for (int j = 0; j < student; j++) {
				arr[j] = sc.nextInt();
			}
			
			double avg = Arrays.stream(arr).average().getAsDouble();
			int count = (int) Arrays.stream(arr).filter(it -> it > 3).count();
			double percnt = (double) count / student;
			System.out.printf("%.3f%%\n", percnt * 100);
		} 
	}
}