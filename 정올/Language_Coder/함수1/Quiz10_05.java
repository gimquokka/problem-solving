import java.util.Scanner;

public class Quiz10_05 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] arr = new int[4][4];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        sumOfScore(arr);
    }

    public static void sumOfScore(int[][] arr) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                arr[i][3] += arr[i][j];
            }
        }

        for (int y = 0; y < 4; y++) {
            for (int x = 0; x < 3; x++) {
                arr[3][y] += arr[x][y];
            }
        }

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
