package programmers.lv1;

public class 시저암호 {
    public String solution(String s, int n) {
    	StringBuilder answer = new StringBuilder();
        
    	for (char c : s.toCharArray()) {
    		char pwd = ' ';
    		
    		if ((Character.isUpperCase(c) && 'Z' < c + n) || (Character.isLowerCase(c) && 'z' < c + n))
    			pwd = (char) (c + n - 26);
    		else if (c != ' ')
    			pwd = (char) (c + n);
    		
    		answer.append(pwd);
		}
        return new String(answer);
    }
}
