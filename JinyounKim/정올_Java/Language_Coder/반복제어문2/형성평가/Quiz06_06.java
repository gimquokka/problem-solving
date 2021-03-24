import java.util.Scanner;

public class Quiz06_06 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int a, b;
        int s = 0, e = 0;
        int sum = 0, cnt = 0;

        a = input.nextInt();
        b = input.nextInt();

        s = Math.min(a, b);
        e = Math.max(a, b);

        for (int i = s; i < e + 1; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum += i;
                cnt += 1;
            }
        }

        System.out.println("합계 : " + sum);
        System.out.printf("평균 : %.1f", sum / (double) cnt);
    }
}
