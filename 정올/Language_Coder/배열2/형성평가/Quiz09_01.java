import java.util.Scanner;

public class Quiz09_01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[6];

        for (int i = 0; i < 10; i++) {
            arr[sc.nextInt() - 1]++;
        }

        for (int i = 1; i <= 6; i++) {
            System.out.println(i + " : " + arr[i - 1]);
        }
    }
}
