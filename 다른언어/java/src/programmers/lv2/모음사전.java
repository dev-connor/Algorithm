package programmers.lv2;

public class 모음사전 {
	StringBuilder stack = new StringBuilder();
	int n = 0;
	String[] alpha = {"A", "E", "I", "O", "U"};
	int answer;
	
    public int solution(String word) {
        dfs(word);
        return answer;
    }

	private int dfs(String word) {
		if (stack.length() == 5) {
			if (word.equals(new String(stack))) answer = n;
			n++;
		}
		else {
			for (int i = 0; i < 5; i++) {
				if (i == 0) {
					if (word.equals(new String(stack))) answer = n;
					n++;
				}
				stack.append(alpha[i]);
				dfs(word);
				stack.deleteCharAt(stack.length() - 1);
			}
		}
		return -1;
	}
}