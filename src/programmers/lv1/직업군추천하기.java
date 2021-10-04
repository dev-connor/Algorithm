package programmers.lv1;

import java.util.Arrays;
import java.util.Collections;

public class 직업군추천하기 {
    public String solution(String[] table, String[] languages, int[] preference) {
    	String answer = "";
        int max = 0;
        String[][] jobs = new String[5][6];
        Arrays.sort(table, Collections.reverseOrder());
        
        for (int i = 0; i < table.length; i++) {
			jobs[i] = table[i].split(" ");
		}

        for (String[] job : jobs) {
        	int sum = 0;
        	int idx = 0;
        	for (String l : languages) {
        		for (int i = 1; i < job.length; i++) {
        			if (job[i].equals(l)) {
        				sum += (6 - i) * preference[idx];
        				break;
        			}
        		}
        		idx++;
			}
        	if (max <= sum) {
        		max = sum;
        		answer = job[0];
        	}
        	System.out.printf("%s: %d\n", job[0], sum);
		}
        return answer;
    }
}
