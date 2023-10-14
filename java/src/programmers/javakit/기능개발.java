package programmers.javakit;

import java.util.ArrayList;

public class 기능개발 {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
    	ArrayList<Integer> answer = new ArrayList<>();
        int[] periods = new int[speeds.length];
        int max = -1;
        int count = 1;
        
        for (int i = 0; i < periods.length; i++) 
			periods[i] = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);
        
        for (int i : periods) {
			if (max == -1) {
				max = i;
			} else if (max >= i) {
				count++;
			} else {
				answer.add(count);
				count = 1;
				max = i;
			}
		}
        answer.add(count);
		return answer;
    }
}
