package programmers.lv1;

import java.util.Arrays;

class 모의고사 {
    public int[] solution(int[] answers) {
    	int[] answer = new int[3];
        int[] counts = new int[3];
        int[][] randoms = {
        		{1, 2, 3, 4, 5},
        		{2, 1, 2, 3, 2, 4, 2, 5},
        		{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        int max = -1;
        int idx = 1;
        
        for (int student = 0; student < counts.length; student++) {
        	for (int quiz = 0; quiz < answers.length; quiz++) {
				if (answers[quiz] == randoms[student][quiz % randoms[student].length]) counts[student]++;
			}
        	if (max < counts[student]) {
        		max = counts[student];
        		answer[0] = student + 1;
        	} else if (max == counts[student]) answer[idx++] = student + 1; 
		}
        return Arrays.copyOf(answer, idx);
    }
}