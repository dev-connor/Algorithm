package baekjoon.step.브루트포스;

import java.util.Scanner;

public class 블랙잭 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] cards = new int[n];
		
		for (int i = 0; i < n; i++) {
			cards[i] = sc.nextInt();
		}
		int answer = getMax(cards, m);
		System.out.println(answer);
	}

	private static int getMax(int[] cards, int m) {
		int max = 0;
		
		for (int i = 0; i < cards.length - 2; i++) {
			for (int j = i + 1; j < cards.length - 1; j++) {
				for (int k = j + 1; k < cards.length; k++) {
					int sum = cards[i] + cards[j] + cards[k];
					
					if (sum > max && sum <= m) {
						max = sum;
					}
				}
			}
		}
		return max;
	}
}
