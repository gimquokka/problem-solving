import java.util.Scanner;

public class Quiz10_12 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        System.out.print("원의 반지름 : ");
        double r = sc.nextDouble();

        System.out.printf("원의 넓이 = %.3f", findCircleArea(r));
    }

    public static double findCircleArea(double r) {
        final double PI = 3.141592;
        return r*r*PI;
    }
}
