package programmers.javakit;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class 다리를_지나는_트럭 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
    	Queue<Integer> q = new LinkedList<Integer>();
    	int idx = 0;
    	int time = 0;
    	int sum = 0;
    	
    	while (idx < truck_weights.length) {
    		time++;
    		
    		if (q.size() == bridge_length) 
    			sum -= q.poll();
    		
    		if (sum + truck_weights[idx] <= weight) {
    			q.offer(truck_weights[idx]);
    			sum += truck_weights[idx];
    			idx++;
    		} else {
    			q.offer(0);
    		}
    	}
        return time + bridge_length;
    }
}
