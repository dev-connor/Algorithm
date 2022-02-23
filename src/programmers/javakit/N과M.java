package programmers.javakit;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class N과M {
	private static int TO;
	private static int NUMBER_OF;
	static ArrayList<Integer> list = new ArrayList<>();
	private static BufferedWriter bw;

	public static void main(String[] args) throws IOException {
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		Scanner sc = new Scanner(System.in);
		TO = sc.nextInt();
		NUMBER_OF = sc.nextInt();
		
		dfs();
		bw.flush();
	}

	private static void dfs() throws IOException {
		if (list.size() == NUMBER_OF) {
			for (Integer it : list) bw.write(it + " ");
			bw.write("\n");
		} else {
			for (int i = 1; i <= TO; i++) {
				if (!list.contains(i)) {
					list.add(i);
					dfs();
					list.remove(list.indexOf(i));
				}
			}
		}
	}
}