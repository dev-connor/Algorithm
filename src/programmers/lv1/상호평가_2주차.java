package programmers.lv1;

public class 상호평가_2주차 {
    public String solution(int[][] scores) {
        String answer = "";
        
        for (int i = 0; i < scores.length; i++) {
        	int sum = 0;
        	int max = 0;
        	int min = 100;
        	
        	for (int j = 0; j < scores.length; j++) {
        		int score = scores[j][i];
        		
        		sum += score;
        		if (i != j) {
        			if (min > score) min = score;
        			if (max < score) max = score;
        		}
			}
        	double avg = selfRating(scores[i][i], max, min) ? (double) sum / scores.length :
        		(double) (sum - scores[i][i]) / (scores.length - 1);
        	answer += getGrade(avg);
		}
        return answer;
    }

	private boolean selfRating(int mine, int max, int min) {
		return mine > max || mine < min ? false : true;
	}

	public String getGrade(double avg) {
		return avg >= 90 ? "A" : avg >= 80 ? "B" : avg >= 70 ? "C" : avg >= 50 ? "D" : "F";
	}
}
