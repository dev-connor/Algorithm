package programmers.lv2;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;

public class 게임_맵_최단거리 {
	static int[][] maps;
	Queue<Pos> q = new LinkedList<>();
	HashSet<Pos> visited = new HashSet<>();
	int[] x = {0, 1, 0, -1};
	int[] y = {1, 0, -1, 0};

	public int solution(int[][] maps) {
		this.maps = maps;
		visited.add(new Pos(0, 0, 1));
		q.offer(new Pos(0, 0, 1));
		return bfs();
	}

	private int bfs() {
		while (!q.isEmpty()) {
			Pos p = q.poll();
			
			if (p.x == maps.length - 1 && p.y == maps[0].length - 1) {
				return p.step;
			}
			
			for (int i = 0; i < 4; i++) {
				Pos newP = new Pos(p.x + x[i], p.y + y[i], p.step + 1);
				if (canMove(newP)) {
					q.offer(newP);
					visited.add(newP);
				}
			}
		}
		return -1;
	}

	// 맵 안이고 벽이 아니고 지나가지 않았던 길을 갑니다.
	private boolean canMove(Pos p) {
		if (0 <= p.x && p.x < maps.length && 0 <= p.y && p.y < maps[0].length 
				&& maps[p.x][p.y] == 1
				&& !visited.contains(p)) 
			return true;
		else return false;
	}
}

class Pos {
	int x;
	int y;
	int step;
	
	public Pos(int x, int y, int step) {
		this.x = x;
		this.y = y;
		this.step = step;
	}

	@Override
	public boolean equals(Object o) {
		Pos p = (Pos) o;
		if (x == p.x && y == p.y) return true;
		else return false;
	}

	@Override
	public int hashCode() {
		return Objects.hash(x, y);
	}

	@Override
	public String toString() {
		return "Pos [x=" + x + ", y=" + y + ", step=" + step + "]";
	}
}
