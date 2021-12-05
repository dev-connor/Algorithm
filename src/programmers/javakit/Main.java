package programmers.javakit;

import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		주식가격 s = new 주식가격();
		
		int[] arr = {1, 2, 3, 2, 3};
		int[] arr2 = {4, 3, 1, 1, 0};
		
		
		System.out.println(Arrays.toString(s.solution(arr)));
	}
	

}
