package baekjoon.step.재귀;

import java.util.Scanner;

public class 팩토리얼 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int answer = fac(sc.nextInt());
		System.out.println(answer);
	}

	private static int fac(int n) {
		if (n <= 1) return 1;
		else 
			return n * fac(n - 1);
	}
}