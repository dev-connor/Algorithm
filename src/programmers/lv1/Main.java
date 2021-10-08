package programmers.lv1;

import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		행렬의덧셈 s = new 행렬의덧셈();
		int[][] arr1 = {{1,2},{2,3}};
		int[][] arr2 = {{3,4},{5,6}};
//		System.out.println(s.solution(arr1, arr2));
		for (int[] is : s.solution(arr1, arr2)) {
			System.out.println(Arrays.toString(is));
		}
		
		arr2[1][1] = 10;
		

		for (int[] is : s.solution(arr1, arr2)) {
			System.out.println(Arrays.toString(is));
		}
		
	}
}
