import java.util.Scanner;

public class Quiz08_04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = 0;
        int[] arr = new int[100];

        for (int i = 0; i < 100; i++) {
            arr[i] = sc.nextInt();

            if (arr[i] == -1) {
                if (i >= 3) {
                    System.out.printf("%d %d %d", arr[i - 3], arr[i - 2], arr[i - 1]);
                } else {
                    for (int j = 0; j < i; j++) {
                        System.out.print(arr[j] + " ");
                    }
                }
                break;

            }
        }
    }
}
