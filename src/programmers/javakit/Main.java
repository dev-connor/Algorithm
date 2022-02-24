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
		더_맵게 s = new 더_맵게();
		int[] arr = {1, 2, 3, 9, 10, 12};
		String[][] arr2 = {{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};
		
		System.out.println(s.solution(arr, 7));
		
	}
}