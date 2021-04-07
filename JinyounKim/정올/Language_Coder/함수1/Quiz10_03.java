import java.util.Scanner;

public class Quiz10_03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        printSquareNum(n);
    }

    public static void printSquareNum(int n) {
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            cnt++;
            for (int j = 1; j <=n ; j++) {
                System.out.print(cnt * j + " ");
            }
            System.out.println();
        }
    }
}
