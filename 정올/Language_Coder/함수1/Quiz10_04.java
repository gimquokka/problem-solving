import java.util.Scanner;

public class Quiz10_04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(diffSquareNums(a, b));
    }

    public static int diffSquareNums(int a, int b) {
        return Math.abs(a * a - b * b);
    }
}
