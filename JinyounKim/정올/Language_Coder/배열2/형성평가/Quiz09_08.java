import java.util.Scanner;

public class Quiz09_08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] arr = new int[4][2];
        int[] horizonAvg = new int[4];
        int[] verticalAvg = new int[2];
        int totAvg = 0;

        int a = 0;
        int b = 0;


        for (int i = 0; i < 4; i++) {
            a = sc.nextInt();
            b = sc.nextInt();

            horizonAvg[i] = (a + b) / 2;
            verticalAvg[0] += a;
            verticalAvg[1] += b;
            totAvg += a + b;
        }

        for (int i : horizonAvg) {
            System.out.print(i + " ");
        }
        System.out.println();

        for (int i : verticalAvg) {
            System.out.print(i/4 + " ");
        }
        System.out.println();

        System.out.println(totAvg/8);
    }
}

