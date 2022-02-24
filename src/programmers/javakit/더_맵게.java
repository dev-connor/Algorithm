package programmers.javakit;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class 더_맵게 {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int i : scoville) heap.offer(i);
        
        while (heap.peek() < K) {
        	int first = heap.poll();
        	if (heap.peek() == null) return -1;
        	int newOne = mix(first, heap.poll());
        	heap.offer(newOne);
        	answer++;
        }
        return answer;
    }

	private int mix(Integer f1, Integer f2) {
		return f1 + 2 * f2;
	}
}
