package programmers.lv1;

public class 두정수사이의합 {
    public long solution(int a, int b) {
    	int sum = 0;
    	
        for (int i = a > b ? b : a; i <= (a > b ? a : b); i++) {
			sum += i;
		}
        return sum;
    }
}