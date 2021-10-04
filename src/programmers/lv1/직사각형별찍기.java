package programmers.lv1;

import java.util.Scanner;

public class 직사각형별찍기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        System.out.println(("*".repeat(x)+"\n").repeat(y));
        sc.close();
    }
}
