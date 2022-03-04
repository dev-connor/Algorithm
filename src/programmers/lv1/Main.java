package programmers.lv1;

public class Main {
	public static void main(String[] args) {
		키패드_누르기 s = new 키패드_누르기();
		
		int[] arr = {1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5};
		
		System.out.println(s.solution(arr, "right"));
		
	}
}
