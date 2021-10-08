package baekjoon.step;

import java.util.ArrayList;
import java.util.Scanner;

public class 최댓값2562 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> list = new ArrayList<>();

		for (int i = 0; i < 9; i++) 
			list.add(sc.nextInt());

		int max = list.stream().mapToInt(i -> i).max().getAsInt();
		System.out.print(max + "\n" + (list.indexOf(max) + 1));
	}
}