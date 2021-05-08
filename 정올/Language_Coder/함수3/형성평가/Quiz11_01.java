import java.util.Scanner;

public class Quiz11_01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        print(n);
    }
    // 100 => 50 => 25 ... 1
    private static void print(int n) {
        // 제귀함수 앞에 중단조건을 반드시 만들어 놓아야함
        if (n == 0) return;
        print(n/2);
        System.out.print(n + " ");
    }
}
