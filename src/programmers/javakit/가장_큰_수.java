package programmers.javakit;

import java.util.Arrays;
import java.util.stream.Stream;

public class 가장_큰_수 {
    public String solution(int[] numbers) {
        StringBuilder str = new StringBuilder();
        
        for (int i : numbers) 
			str.append(i);
        
        int[] sorted = str.chars().sorted().map(i -> i-'0').toArray();
        str.setLength(0);
        
        for (int i = sorted.length - 1; i >= 0; i--) 
        	str.append(sorted[i]);
        	
        return str.toString();
    }
}