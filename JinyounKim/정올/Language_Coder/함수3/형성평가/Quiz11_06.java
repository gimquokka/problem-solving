import java.util.Scanner;

public class Quiz11_06 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int n = a * b * c;

        System.out.println(mulOfDigit(n));
    }

    private static int mulOfDigit(int n) {
        if (n == 0) return 1;
        if (n % 10 == 0) {
            return mulOfDigit(n / 10);
        } else {
            return mulOfDigit(n / 10) * (n % 10);
        }
    }
}


