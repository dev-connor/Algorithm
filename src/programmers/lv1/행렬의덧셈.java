package programmers.lv1;

import java.util.Arrays;

public class 행렬의덧셈 {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = Arrays.stream(arr2).map(int[]::clone).toArray(int[][]::new);
        
        return answer;
    }

}
