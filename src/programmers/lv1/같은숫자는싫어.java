package programmers.lv1;

import java.util.Arrays;

public class 같은숫자는싫어 {
    public int[] solution(int []arr) {
        int[] answer = new int[arr.length];
        int count = 0;

        for (int i = 0; i < arr.length - 1; i++) {
			if (arr[i] != arr[i + 1]) answer[count++] = arr[i];
		}
        answer[count++] = arr[arr.length - 1];
        return Arrays.copyOf(answer, count);
    }
}
