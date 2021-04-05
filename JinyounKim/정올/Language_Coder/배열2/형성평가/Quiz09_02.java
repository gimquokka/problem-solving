import java.util.Scanner;

public class Quiz09_02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int score = 0;
        int perTen = -10;
        int[] arr = new int[11];

        for (int i = 0; i < 100; i++) {
            score = sc.nextInt();

            if (score == 0) break;

            arr[score / 10]++;
        }

        for (int i = 10; i >= 0; i--) {
            if (arr[i] == 0) continue;
            System.out.printf("%d : %d person\n", i*10, arr[i]);
        }
    }
}
