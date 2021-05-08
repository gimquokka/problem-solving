import java.util.Scanner;

public class Quiz11_02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        oddOrEven(n);
    }

    private static void oddOrEven(int n) {
        if (n < 1) return;
        oddOrEven(n - 2);
        System.out.print(n + " ");
    }
}
