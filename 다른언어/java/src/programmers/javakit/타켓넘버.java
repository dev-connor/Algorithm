package programmers.javakit;

import java.util.Stack;

public class 타켓넘버 {
	int[] numbers;
	int target;
	
    public int solution(int[] numbers, int target) {
    	this.numbers = numbers;
    	this.target = target;
    	
    	return dfs(0, 0);
    }

	private int dfs(int sum, int idx) {
		if (idx == numbers.length) {
			if (sum == target) return 1;
			else return 0;
		}
		return dfs(sum + numbers[idx], idx + 1) + dfs(sum - numbers[idx], idx + 1);
	}
}
