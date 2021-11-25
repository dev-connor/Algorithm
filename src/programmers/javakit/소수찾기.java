package programmers.javakit;

import java.util.HashSet;

public class 소수찾기 {
	StringBuilder str = new StringBuilder();
	char[] arr;
	HashSet<Integer> check = new HashSet<>();
	HashSet<Integer> answer = new HashSet<>();

	public int solution(String numbers) {
		arr = numbers.toCharArray();

		dfs();
		return answer.size();
	}

	private void dfs() {
		if (arr.length != str.length()) {
			for (int i = 0; i < arr.length; i++) {
				if (!check.contains(i)) {
					str.append(arr[i]);
					check.add(i);
					
					isPrime(str);
					dfs();
					
					str.deleteCharAt(str.length()-1);
					check.remove(i);
				}
			}
		} 
	}

	private void isPrime(StringBuilder str) {
		int n = Integer.parseInt(new String(str));
		
		for (int i = 2; i <= Math.sqrt(n); i++) {
			if (n % i == 0) return;
		}
		
		if (n >= 2) answer.add(n);
	}
}