package baekjoon.step;

import java.util.Scanner;

public class 한수1065 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int count = 99;

		for (int i = 100; i <= n; i++) {
			char[] arr = String.valueOf(i).toCharArray();
			int d = arr[1] - arr[0];

			for (int j = 1; j < arr.length - 1; j++) {
				if (d != arr[j + 1] - arr[j]) break;
				if (j == arr.length - 2) count++;
			}
		}
		System.out.println(n >= 100 ? count : n);
	}
}