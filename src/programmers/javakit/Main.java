package programmers.javakit;

public class Main {
	public static void main(String[] args) {
		소수찾기 s = new 소수찾기();
		String numbers = "113";
		
		System.out.println(s.solution(numbers));
		

		double b = 24;
		double y = 24;
		double r = (-1 * (-b/2 + 2) + Math.sqrt(Math.pow(-b/2 + 2, 2) - 4 * y)) / 2;
		double r2 = (-1 * (-b/2 + 2) - Math.sqrt(Math.pow(-b/2 + 2, 2) - 4 * y)) / 2;
		System.out.println(r);
		System.out.println(r2);
	}
	

}
