package programmers.lv1;

public class 가운데글자가져오기 {
    public String solution(String s) {
        int half = s.length() / 2;
        
        return s.length() % 2 == 0 ? s.substring(half - 1, half + 1) :
        s.charAt(half) + "";
    }
}