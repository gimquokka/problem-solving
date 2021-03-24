import java.util.Scanner;

public class Quiz06_02 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int a, b, start, end;

        a = input.nextInt();
        b = input.nextInt();

        start = Math.min(a, b);
        end = Math.max(a, b);

        for (int i = start; i < (end + 1); i++) {
            System.out.print(i + " ");
        }
    }
}
