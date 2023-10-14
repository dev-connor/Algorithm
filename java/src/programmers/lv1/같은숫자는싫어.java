package programmers.lv1;

import java.util.ArrayList;
import java.util.Arrays;

public class 같은숫자는싫어 {
    public int[] solution(int []arr) {
    	ArrayList<Integer> list = new ArrayList<>(Arrays.asList(arr[0]));

    	for (int i = 0; i < arr.length - 1; i++) {
			if (arr[i] != arr[i + 1]) list.add(arr[i + 1]);
		}
        return list.stream().mapToInt(i -> i).toArray();
    }
}