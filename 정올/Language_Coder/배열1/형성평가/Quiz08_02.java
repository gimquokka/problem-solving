import java.util.Scanner;

public class Quiz08_02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] inputArray = new int[5];

        for (int i = 0; i < 5; i++) {
            inputArray[i] = sc.nextInt();
        }

        System.out.println(inputArray[0]+inputArray[2]+inputArray[4]);

    }
}
