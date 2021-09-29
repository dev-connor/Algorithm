package programmers.lv1;

import java.util.Arrays;
import java.util.Comparator;

public class 최소직사각형_8주차 {
    public int solution(int[][] sizes) {
        for (int[] size : sizes) if (size[0] < size[1]) rotate(size);
        return Arrays.stream(sizes).max(Comparator.comparingInt(it -> it[0])).get()[0] *
        		Arrays.stream(sizes).max(Comparator.comparingInt(it -> it[1])).get()[1];
    }

	private void rotate(int[] size) {
		int temp = size[0];
		size[0] = size[1];
		size[1] = temp;
	}
}
