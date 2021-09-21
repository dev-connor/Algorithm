package programmers.lv1;

public class 부족한금액계산하기_1주차 {
    public long solution(int price, int money, int count) {
        long sum = 0;
        
        for (int i = 1; i <= count; i++) {
			sum += i * price;
		}
        return sum > money ? sum - money : 0;
    }
}
