import java.util.Scanner;

public class Quiz08_09 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[110];
        int num = 0;
        int cnt = 0;


        for (int i = 0; i < 100; i++) {
            num = sc.nextInt();
            if (num == 0) break;
            arr[i] = num;
            cnt++;
        }

        System.out.println(cnt + "개");

        for (int i = 0; i < 100; i++) {
            if (arr[i] == 0) break;
            if (arr[i] % 2 == 1) {
                System.out.print(arr[i] * 2 + " ");
            } else {
                System.out.print(arr[i]/2 + " ");
            }
        }
    }
}
