import java.util.Scanner;

public class Quiz07_04 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * n - 1 - 2 * i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        for (int i = 0; i < n - 1; i++) {
            for (int j = n - 2 - i; j > 0; j--) {
                System.out.print(" ");
            }
            for (int j = 0; j < 3 + 2 * i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

}

