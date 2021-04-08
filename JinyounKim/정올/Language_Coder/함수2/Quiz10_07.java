import java.util.*;

public class Quiz10_07 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        double a = sc.nextDouble();
        double b = sc.nextDouble();

        if (a > b) {
            double temp = a;
            a = b;
            b = temp;
        }

        double sqrt_a = Math.sqrt(a);
        double sqrt_b = Math.sqrt(b);

        int intA = (int) Math.ceil(sqrt_a);
        int intB = (int) Math.floor(sqrt_b);

        System.out.println(intB - intA + 1);
    }
}
