import java.util.Scanner;

public class Quiz05_11 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n, cnt = 0;

        while (true) {
            n = input.nextInt();
            if (n == 0) break;
            if (n%3 == 0 || n%5 == 0) continue;
            cnt++;
        }

        System.out.print(cnt);
    }
}