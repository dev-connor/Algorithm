package programmers.javakit;

import java.util.HashSet;
import java.util.List;

public class 전화번호_목록 {
    public boolean solution(String[] phone_book) {
        HashSet<String> set = new HashSet<>(List.of(phone_book));
        
        for (String p_num : phone_book) {
        	for (int i = 1; i < p_num.length(); i++) {
        		if (set.contains(p_num.substring(0, i)))
        			return false;
			}
		}
        return true;
    }
}
