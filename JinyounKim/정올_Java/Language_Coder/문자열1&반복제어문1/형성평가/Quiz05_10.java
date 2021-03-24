import java.util.Scanner;

public class Quiz05_10 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int even = 0;
        int odd = 0;
        int n, sum = 0, cnt = 0;

        while (true) {
            n = input.nextInt();
            if (n < 0 || 100 < n) break;

            sum += n;
            cnt++;
        }

        System.out.println("합계 : " + sum + '점');
        System.out.printf("평균 : %.1f점", ((double) sum)/cnt);
    }
}