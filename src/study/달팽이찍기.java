package study;

public class 달팽이찍기 {
	public void fillSnail(int[][] arr) {
	    int row = 0, col = -1, n = 1, move = arr.length;
	    boolean plus = true, widthwise = true;

	    while (move > 0) {
	        for (int i = 0; i < move; i++) {
	            if (widthwise) col += plus ? 1 : -1; 
	            else row += plus ? 1 : -1; 
	            arr[row][col] = n++;
	        }

	        if (widthwise) move--;
	        if (!widthwise) plus = !plus;
	        widthwise = !widthwise;
	    }
	}
}