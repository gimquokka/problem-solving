import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Quiz08_10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Integer[] arr = new Integer[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr, Comparator.reverseOrder());

        for (int ele : arr) {
            System.out.println(ele);
        }
    }
}
