import java.util.Scanner;

public class Quiz08_03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        int odd = 0;
        int even = 0;

        for (int i = 0; i < 10; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < 10; i += 2) {
            odd += arr[i];
        }
        for (int i = 1; i < 10; i += 2) {
            even += arr[i];
        }

        System.out.println("홀수 번째 합 : " + odd);
        System.out.println("짝수 번째 합 : " + even);
    }
}
