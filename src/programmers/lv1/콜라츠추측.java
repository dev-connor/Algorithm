package programmers.lv1;

public class 콜라츠추측 {
    public int solution(int num) {
    	long n = num;
        int count = 0;
        
        while (n != 1) {
        	n = n % 2 == 0 ? n/2 : n*3 + 1;
        	if (++count == 500) return -1;
        }
        return count;
    }
}
