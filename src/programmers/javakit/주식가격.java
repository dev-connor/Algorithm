package programmers.javakit;

public class 주식가격 {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        for (int i = 0; i < prices.length - 1; i++) {
        	int price = prices[i];
        	
        	for (int j = i + 1; j < prices.length; j++) {
        		int nextPrice = prices[j];
        		if (price > nextPrice) {
        			answer[i] = j - i;
        			break;
        		}
        		
			}
        	if (answer[i] == 0)
        		answer[i] = prices.length - 1 - i;
		}
        return answer;
    }
}