package baekjoon.step;

import java.util.ArrayList;
import java.util.Scanner;

public class 평균1546 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> list = new ArrayList<>();
		int n = sc.nextInt();

		for (int i = 0; i < n; i++) 
			list.add(sc.nextInt());

		int max = list.stream().mapToInt(i -> i).max().getAsInt();
		double avg = list.stream().mapToDouble(i -> (double) i / max * 100).average().getAsDouble();
		System.out.println(avg);
	}
}