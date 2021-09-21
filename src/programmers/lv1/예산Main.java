package programmers.lv1;

import java.util.Arrays;

class 예산 {
    public int solution(int[] d, int budget) {
    	Arrays.sort(d);
        int i;
        
        for (i = 0; i < d.length && budget - d[i] >= 0; i++) {
			budget -= d[i];
		}
        return i;
    }
}