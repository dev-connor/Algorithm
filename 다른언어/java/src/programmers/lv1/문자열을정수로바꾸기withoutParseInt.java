package programmers.lv1;

public class 문자열을정수로바꾸기withoutParseInt {
    public int solution(String s) {
    	String absStr = s.matches("[+-].+") ? s.substring(1) : s;
    	int figures = (int) Math.pow(10, absStr.length() - 1);
    	int abs = 0;
    	
    	for (char c : absStr.toCharArray()) {
    		abs += figures * (c - '0');
    		figures /= 10;
		}
    	return s.startsWith("-") ? -abs : abs;
    }
}