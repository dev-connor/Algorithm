package programmers.lv2;

import java.util.Arrays;
import java.util.stream.Stream;

public class 최댓값과_최솟값 {
    public String solution(String s) {
        int[] arr = Stream.of(s.split(" ")).mapToInt(Integer::parseInt).toArray();
        int min = Arrays.stream(arr).min().getAsInt();
        int max = Arrays.stream(arr).max().getAsInt();
        return String.format("%d %d", min, max);
    }
}
