import java.util.Scanner;

public class Quiz11_03 {
    static int n;
    static int arr[];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        int m = sc.nextInt();

        arr = new int[n + 1];

        dice(1, m);
    }

    private static void dice(int level, int m) {
        if (level > n) {
//            if (Arrays.stream(arr).sum() == m) printout();
            if (_sum(arr) == m) printout();
            return;
        }

        for (int i = 1; i <= 6; i++) {
//            System.out.println(level);
            arr[level] = i;
            dice(level+1, m);
        }
    }

    private static int _sum(int[] arr) {
        int sum = 0;
        for (int e: arr) sum += e;
        return sum;
    }

    private static void printout() {
        for (int i = 1; i <= n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}


