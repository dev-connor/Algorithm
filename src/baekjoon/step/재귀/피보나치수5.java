package baekjoon.step.재귀;

import java.util.Scanner;

public class 피보나치수5 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int answer = pivo(sc.nextInt());
		System.out.println(answer);
	}

	private static int pivo(int n) {
		if (n <= 1) return n;
		else return pivo(n - 1) + pivo(n - 2);
	}

}
