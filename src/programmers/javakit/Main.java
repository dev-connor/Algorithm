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
		H_Index s = new H_Index();
		int[] arr = {3, 0, 6, 1, 5};
		String[][] arr2 = {{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};
		
		System.out.println(s.solution(arr));
		
	}
}