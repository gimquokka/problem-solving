import java.util.Scanner;

public class Quiz10_10 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        double sum, roundSum;

        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();

        sum = a + b + c;

        System.out.println((int) Math.round(sum/3.0));

        roundSum = Math.round(a) + Math.round(b) + Math.round(c);

        System.out.println((int) Math.round(roundSum/3.0));
    }
}
