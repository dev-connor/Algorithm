package programmers.lv1;

import java.util.ArrayList;

public class 나누어_떨어지는_숫자_배열 {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i : arr) {
			if (i % divisor == 0)
				list.add(i);
		}
        list.sort(null);
        if (list.isEmpty()) list.add(-1);
        return list.stream().mapToInt(i -> i).toArray();
    }
}
