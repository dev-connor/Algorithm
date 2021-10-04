package programmers.lv1;

public class 하샤드수 {
	int sum = 0;
    public boolean solution(int x) {
      String.valueOf(x).chars().forEach(it -> sum += it - '0');
      return x % sum == 0;
    }
}