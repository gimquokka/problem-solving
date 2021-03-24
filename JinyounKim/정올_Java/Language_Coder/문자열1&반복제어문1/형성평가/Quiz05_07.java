import java.util.Scanner;

public class Quiz05_07 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String word = input.nextLine();

        String[] arr = word.split(" ");

        for (int i = 0; i < arr.length; i++) {
            System.out.println((i + 1) + ". " + arr[i]);
        }
    }
}