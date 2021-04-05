import java.util.Scanner;

public class Quiz09_09 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] arr = new int[10][10];

        int n = sc.nextInt();

        for (int i = 0; i < 10; i++) arr[i][0] = 1;

        for (int i = 1; i < 10; i++) {
            for (int j = 1; j <= i; j++) {
                arr[i][j] += arr[i - 1][j - 1];
                if (j != i) {
                    arr[i][j] += arr[i - 1][j];
                }
            }
        }

        for (int i = n-1; i > -1; i--) {
            for (int j = 0; j <= i; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

    }
}


