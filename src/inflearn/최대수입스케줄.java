package inflearn;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
	int solution(int n, int[][] arr) {
		Arrays.sort(arr, (o1, o2) -> o2[1] - o1[1]);
		int max = arr[0][1];
		PriorityQueue<Integer> q = new PriorityQueue<>(Comparator.reverseOrder());
		int income = 0;
		int idx = 0;

		for (int i = max; i >= 1; i--) {
		    for (; idx < arr.length; idx++) {
		        if (arr[idx][1] == i) q.offer(arr[idx][0]); 
		        else break;
		    }
		    if (!q.isEmpty()) income += q.poll();
		}
		return income;
	}
}