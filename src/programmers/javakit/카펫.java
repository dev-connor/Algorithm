package programmers.javakit;

public class 카펫 {
    public int[] solution(int brown, int yellow) {
        int[] answer = {
        		(int) ((-1 * (-brown/2 + 2) + Math.sqrt(Math.pow(-brown/2 + 2, 2) - 4 * yellow)) / 2) + 2
        		, (int) ((-1 * (-brown/2 + 2) - Math.sqrt(Math.pow(-brown/2 + 2, 2) - 4 * yellow)) / 2) + 2
        };
        return answer;
    }
}