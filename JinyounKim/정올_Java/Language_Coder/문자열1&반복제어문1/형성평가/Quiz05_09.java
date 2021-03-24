import java.util.Scanner;

public class Quiz05_09 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int even = 0;
        int odd = 0;
        int n;

        while (true) {
            n = input.nextInt();
            if (n == 0) break;

            if (n%2 == 0) {
                even++;
            }
            else {
                odd++;
            }
        }

        System.out.println("홀수 : " + odd + '개');
        System.out.println("짝수 : " + even + '개');
    }
}