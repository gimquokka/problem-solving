import java.util.Scanner;

public class Quiz06_04 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int sum = 0;

        int n = input.nextInt();

        for (int i = 0; i < n; i++) {
            sum += input.nextInt();
        }

        System.out.printf("%.2f", sum/(double) n);
    }
}
