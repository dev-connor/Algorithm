package programmers.lv1;

import static java.lang.Math.abs;

public class 키패드_누르기 {
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();
        int posL = 10;
        int posR = 12;
        int[] distance = {0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 4};
        
        for (int i : numbers) {
        	if (i == 0) i = 11;
        	
			if (i % 3 == 1) {
				answer.append("L");
				posL = i;
			}
			else if (i % 3 == 0) {
				answer.append("R");
				posR = i;
			}
			else {
				int disL = distance[abs(i - posL)];
				int disR = distance[abs(i - posR)];
				
				if (disL > disR) {
					answer.append("R");
					posR = i;
				} else if (disL < disR) {
					answer.append("L");
					posL = i;
				} else if (hand.equals("right")) {
					answer.append("R");
					posR = i;
				} else {
					answer.append("L");
					posL = i;
				}
			}
		}
        return new String(answer);
    }
}
