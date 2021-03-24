import java.util.Scanner;

public class Quiz03_03 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int a, b;
        a = input.nextInt();
        b = input.nextInt();

        a += 5;
        b *= 2;

        System.out.println("가로 = " + a);
        System.out.println("세로 = " + b);
        System.out.println("넓이 = " + a*b);
    }
}
