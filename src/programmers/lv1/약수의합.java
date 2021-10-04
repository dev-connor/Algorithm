package programmers.lv1;

import static java.lang.Math.sqrt;

public class 약수의합 {
    public int solution(int n) {
    	if (n <= 1) return n;
        int sum = n + 1;
        for (int i = 2; i <= sqrt(n); i++) if (n % i == 0) 
        	sum += i + n/i; 
        return (int) sqrt(n) != sqrt(n) ? sum : sum - (int) sqrt(n);
    }
}