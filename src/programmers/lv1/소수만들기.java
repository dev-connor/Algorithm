package programmers.lv1;

import java.util.HashMap;

class Solution {
	public int solution(int[] nums) {
		HashMap<Integer, Boolean> primes = new HashMap<>();
		int count = 0;

		for (int i = 0; i < nums.length - 2; i++) {
			for (int j = i + 1; j < nums.length - 1; j++) {
				for (int k = j + 1; k < nums.length; k++) {
					int sum = nums[i] + nums[j] + nums[k];
					
					if (primes.containsKey(sum)) count += primes.get(sum) ? 1 : 0;
					else if (isPrime(sum)) {
						count++;
						primes.put(sum, true);
					} else primes.put(sum, false);
				}
			}
		}
		return count;
	}

	private boolean isPrime(int num) {
		for (int i = 2; i <= Math.sqrt(num); i++) {
			if (num % i == 0) return false;
		}
		return true;
	}
}

public class 소수만들기 {
	public static void main(String[] args) {
		Solution s = new Solution();
		int[] nums = {1, 2, 7, 6, 4, 5};
		System.out.println(s.solution(nums));
	}
}
