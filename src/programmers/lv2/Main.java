package programmers.lv2;

import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;

public class Main {
	public static void main(String[] args) {
		다음_큰_숫자 s = new 다음_큰_숫자();
		
		
		int[][] arr1 = {{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,1},{0,0,0,0,1}};
		int[][] arr2 = {{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,0},{0,0,0,0,1}};
		System.out.println(s.solution(15));
	}
}

