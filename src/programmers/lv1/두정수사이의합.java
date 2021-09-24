package programmers.lv1;

public class 두정수사이의합 {
    public long solution(int a, int b) {
        return (long) (Math.abs(b-a)+1)*(a+b)/2;
    }
}