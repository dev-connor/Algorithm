package programmers.lv1;

public class 가운데글자가져오기 {
    public String solution(String s) {
        int len = s.length();
        return s.substring((len-1) / 2, (len+2) / 2);
    }
}