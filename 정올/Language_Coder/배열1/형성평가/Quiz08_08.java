import java.util.Scanner;

public class Quiz08_08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numOfFive = 0;
        int sum = 0;
        int num;

        for (int i = 0; i < 100; i++) {
            num = sc.nextInt();
            if (num == 0) break;
            else if (num % 5 == 0) {
                numOfFive++;
                sum += num;
            };

        }

        System.out.printf("5의 배수 : %d개\n", numOfFive);
        System.out.println("합계 : " + sum);
        System.out.printf("평균 : %.1f", sum/((double) numOfFive));
    }
}
