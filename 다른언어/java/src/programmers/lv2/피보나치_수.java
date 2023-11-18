package programmers.lv2;

import java.math.BigInteger;

public class 피보나치_수 {
    public int solution(int n) {
        BigInteger[] cache = new BigInteger[n + 1]; 
        cache[0] = new BigInteger("0");
        cache[1] = new BigInteger("1");
        
        for (int i = 2; i < cache.length; i++) {
			cache[i] = cache[i - 1].add(cache[i - 2]); 
		}
        return cache[n].remainder(new BigInteger("1234567")).intValue();
    }
}
