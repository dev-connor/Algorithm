package programmers.javakit;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.SortedSet;
import java.util.stream.Stream;

public class Main {
	public static void main(String[] args) {
		전화번호_목록 s = new 전화번호_목록();
		String[] arr = {"12","123","1235","567","88"};
		
		System.out.println(s.solution(arr));
		
	}
}