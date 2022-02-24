package programmers.javakit;

import java.util.Arrays;

public class H_Index {
    public int solution(int[] citations) {
        int n = citations.length;
        Arrays.sort(citations);
        
        for (int i = 0; i < citations.length; i++) {
			if (citations[i] >= n - i) {
				return n - i;
			}
		}
        return 0;
    }
}
