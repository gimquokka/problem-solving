import java.util.Scanner;

public class Quiz10_06 {
    static int[] arr;

    public static void main(String[] args) {
        input();
        sort();
        print();
    }

    public static void input() {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
    }

    public static void sort() {
        int temp;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length - 1; j++) {
                if (arr[j] < arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static void print() {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
