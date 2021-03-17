import java.util.Scanner;

public class Quiz04_01 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int a, b;
        a = input.nextInt();
        b = input.nextInt();

        System.out.println(Math.abs(a - b));
    }
}
