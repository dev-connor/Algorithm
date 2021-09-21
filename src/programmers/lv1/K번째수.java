package programmers.lv1;

import java.util.Arrays;

public class K번째수 {
	public int[] solution(int[] array, int[][] commands) {
		int[] answer = new int[commands.length];
		int idx = 0;

		for (int[] c : commands) {
			int st = c[0] - 1;
			int end = c[1];
			int k = c[2] - 1;
			int[] slice = Arrays.copyOfRange(array, st, end);
			Arrays.sort(slice);
			answer[idx++] = slice[k];
		}
		return answer;
	}
}