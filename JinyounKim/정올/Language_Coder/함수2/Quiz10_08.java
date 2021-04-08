import java.util.*;

public class Quiz10_08 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        // int[] arr = new int[5];
        int sum = 0;

        for (int i = 0; i < 5; i++){
            sum += Math.abs(sc.nextInt());
        }

        System.out.println(sum);
    }
}
