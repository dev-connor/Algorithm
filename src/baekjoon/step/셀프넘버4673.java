package baekjoon.step;

import java.util.HashSet;

public class 셀프넘버4673 {
	public static void main(String[] args) {
		HashSet<Integer> set = new HashSet<>();

		for (int i = 1; i < 10000; i++) {
			int sum = i;

			for (char c : String.valueOf(i).toCharArray()) 
				sum += c - '0';
			set.add(sum);
		}

		for (int i = 1; i <= 10000; i++) 
			if (!set.contains(i)) System.out.println(i);
	}
}