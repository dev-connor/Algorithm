package programmers.lv1;

public class 문자열다루기기본 {
    public boolean solution(String s) {
    	return s.matches("\\d{4}|\\d{6}") ? true : false;
    }
}