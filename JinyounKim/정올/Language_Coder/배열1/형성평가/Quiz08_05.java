import java.util.Scanner;

public class Quiz08_05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double sum = 0;

        for (int i = 0; i < 6; i++) {
            sum += sc.nextDouble();
        }

        System.out.printf("%.1f", sum/6.0);


    }
}
