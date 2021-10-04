package programmers.lv1;

public class Main {
	public static void main(String[] args) {
		직업군추천하기 s = new 직업군추천하기();
		String str = "Zbcdefg";
		String[] table = {"SI JAVA JAVASCRIPT SQL PYTHON C#", 
		                   "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
		                   "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
		                   "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", 
		                   "GAME C++ C# JAVASCRIPT C JAVA"};
		String[] languages = {"PYTHON", "C++", "SQL"};
		int[] preference = {7, 5, 5};
		System.out.println(s.solution(table, languages, preference));
		

		
	}
}
