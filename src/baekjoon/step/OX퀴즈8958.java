package baekjoon.step;

import java.util.Scanner;

public class OX퀴즈8958 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		for (int i = 0; i < n; i++) {
			String quiz = sc.next();
			int point = 0;
			int sum = 0;

			for (char q : quiz.toCharArray()) {
				if (q == 'O') {
					point++;
					sum += point;
				}
				else point = 0;
			}
			System.out.println(sum);
		} 
	}
}