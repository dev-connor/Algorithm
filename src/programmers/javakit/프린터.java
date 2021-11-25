package programmers.javakit;

import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

public class 프린터 {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
        
        for (Integer i : priorities) q.offer(i);
        int max =  Collections.max(q);
        
        while (!q.isEmpty()) {
        	if (max > q.peek()) {
        		q.offer(q.poll());
        	} else {
        		answer++;
        		q.poll();
        		
        		if (location == 0) {
        			break;
        		}
        		max = Collections.max(q);
        	}
        	location--;
        	if (location == -1) location = q.size() - 1;
        }
        return answer;
    }
}
