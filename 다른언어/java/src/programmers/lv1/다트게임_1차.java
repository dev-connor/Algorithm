package programmers.lv1;

import java.util.Arrays;

public class 다트게임_1차 {
    public int solution(String dartResult) {
        int n = 0;
        int[] scores = new int[3];
        int idx = -1;
        boolean isTen = false;
        
        for (char c : dartResult.toCharArray()) {
        	if (Character.isDigit(c)) {
        		n = isTen ? 10 : c - '0';
        		if (!isTen) idx++;
        		isTen = true;
        	} else if (Character.isAlphabetic(c)) {
        		scores[idx] = (int) Math.pow(n, c == 'S' ? 1 : c == 'D' ? 2 : 3);
        		isTen = false;
        	}
        	else {
        		scores[idx] *= c == '*' ? 2 : -1;
        		if (c == '*' && idx != 0) scores[idx - 1] *= 2;
        	}
		}
        return Arrays.stream(scores).sum();
    }
}