package programmers.lv2;

public class 조이스틱 {
    public int solution(String name) {
        int answer = 0;

        for (int i = 0; i < name.length(); i++) {
            int alpha = name.charAt(i) - 'A';
            answer += alpha >= 14 ? 26 - alpha : alpha;
        }

        int f = forward(name);
        int b = backward(name);
        int fb = forback(name);

        System.out.printf("%d %d %d", f, b, fb);
        System.out.println();
        answer += Math.min(f, Math.min(b, fb));
        return answer;
    }


    private int forward(String name) {
        int move = 0;
        for (int i = 1; i < name.length(); i++) {
            if (name.charAt(i) != 'A') move = i;
        }
        return move;
    }

    private int backward(String name) {
        int move = 0;
        for (int i = name.length() - 1; i > 0; i--) {
            if (name.charAt(i) != 'A') move = name.length() - i;
        }
        return move;
    }

    private int forback(String name) {
        int forward = 0;
        int backward = 0;

        for (int i = 1; i <= name.length() / 2; i++) {
            if (name.charAt(i) != 'A') forward = i;
        }
        for (int i = name.length() - 1; i > name.length() / 2; i--) {
            if (name.charAt(i) != 'A') backward = name.length() - i;
        }
        return Math.min(2 * forward + backward, forward + 2 * backward);
    }
}