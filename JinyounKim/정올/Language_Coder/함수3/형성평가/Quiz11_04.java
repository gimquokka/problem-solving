import java.util.Scanner;

public class Quiz11_04 {
    static int n;
    static int arr[] = new int[101];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        arr[1] = 1;
        arr[2] = 2;

        f(n);

        System.out.println(arr[n]);
    }

    /*
    음... 어떻게 풀어야할까?
    피보나치와 같이 구현!
     */
    private static int f(int level) {
        if (arr[level] == 0) return arr[level] = f(level - 1) * f(level - 2) % 100;
        return arr[level];
    }
}


