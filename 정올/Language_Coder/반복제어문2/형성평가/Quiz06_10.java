import java.util.Scanner;

public class Quiz06_10 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int a = input.nextInt();
        int b = input.nextInt();

        for (int i = 1; i < 10; i++) {
            if (a > b) {
                for (int j = a; j > b - 1; j--) {
                    System.out.printf("%d * %d = %2d   ", j, i, i * j);
                }
                System.out.println();
            } else {
                for (int j = a; j < b + 1; j++) {
                    System.out.printf("%d * %d = %2d   ", j, i, i * j);
                }
                System.out.println();
            }
        }

    }
}
