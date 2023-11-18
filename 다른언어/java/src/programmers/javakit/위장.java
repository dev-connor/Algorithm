package programmers.javakit;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;

public class 위장 {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>();
        
        for (String[] c : clothes) {
        	map.put(c[1], map.getOrDefault(c[1], 0) + 1);
		}
        Iterator<Integer> ir = map.values().iterator();
        
        while (ir.hasNext())
        	answer *= ir.next() + 1;
        
        return answer - 1;
    }
}
