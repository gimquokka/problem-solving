import java.util.Scanner;

public class Quiz08_01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[] inputArray = new char[10];

        for (int i = 0; i < 10; i++) {
            inputArray[i] = sc.next().charAt(0);
        }

        for (int i = 9; i >= 0; i--) {
            System.out.print(inputArray[i] + " ");
        }
    }
}
