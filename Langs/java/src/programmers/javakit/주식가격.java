package programmers.javakit;

public class 주식가격 {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        for (int i = 0; i < answer.length - 1; i++) {
            int sec = 0;

            for (int j = i + 1; j < answer.length; j++) {
                sec++;

                if (prices[i] > prices[j]) break;
            }
            answer[i] = sec;
        }
        return answer;
    }
}