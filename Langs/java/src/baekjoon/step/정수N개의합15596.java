package baekjoon.step;

import java.util.Arrays;

class Test {
	long sum;
	
	long sum(int[] a) {
		Arrays.stream(a).forEach(i -> sum += i);
		return sum;
	}
}