package programmers.lv1;

public class Main {
	public static void main(String[] args) {
		상호평가_2주차 s = new 상호평가_2주차();
		int[][] scores = {
				{100, 90, 98, 88, 65},
				{50, 45, 99, 85, 77},
				{47, 88, 95, 80, 67},
				{61, 57, 100, 80, 65},
				{24, 90, 94, 75, 65}
		};
		System.out.println(s.solution(scores));
	}
}
