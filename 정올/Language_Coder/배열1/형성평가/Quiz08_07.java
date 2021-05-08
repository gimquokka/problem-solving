import java.util.Scanner;

public class Quiz08_07 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input = 0;
        int max = -1000;
        int min = 1000;

        for (int i = 0; i < 100; i++) {
            input = sc.nextInt();
            if (input == 999) break;
            max = Math.max(max, input);
            min = Math.min(min, input);
        }

        System.out.println("최대값 : " + max);
        System.out.println("최소값 : " + min);
    }
}
