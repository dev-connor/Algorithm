package programmers.javakit;

public class 큰_수_만들기 {
	static String number;
	
    public String solution(String number, int k) {
    	this.number = number;
        int maxIdx = -1;
        int digit = number.length() - k;
        int i = 0;
        StringBuilder answer = new StringBuilder();
        
        while (answer.length() < digit) {
        	maxIdx = findMax(maxIdx + 1, k + i++);
        	answer.append(number.charAt(maxIdx));
        }
        return new String(answer);
    }

	private int findMax(int start, int end) {
		int max = -1;
		int idx = -1;
		
		for (int i = start; i <= end; i++) {
			if (max < number.charAt(i)) {
				max = number.charAt(i);
				idx = i;
			}
		}
		return idx;
	}
}
