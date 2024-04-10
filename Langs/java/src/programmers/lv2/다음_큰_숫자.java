package programmers.lv2;

import java.util.stream.Stream;

public class 다음_큰_숫자 {
    public int solution(int n) {
        int next = n + 1;
        while (Integer.bitCount(n) != Integer.bitCount(next)) next++;
        return next;
    }
}