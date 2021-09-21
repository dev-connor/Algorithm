package programmers.lv1;

public class 약수의개수와덧셈 {
    public int solution(int left, int right) {
        int sum = 0;
        
        for (int i = left; i <= right; i++) {
			sum += evenDivisor(i) ? i : -i;
		}
        return sum;
    }

	private boolean evenDivisor(int num) {
		return Math.sqrt(num) != (int) Math.sqrt(num);
	}
}