import java.util.Scanner;

public class Quiz11_05 {
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        System.out.println(div(n));

    }

    private static int div(int n) {
        if (n == 1) return 0;
//        System.out.println("n: " + n);
        return div(n % 2 == 0 ? n / 2 : n / 3)+1;
    }
}


