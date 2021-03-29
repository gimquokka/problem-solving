import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int a, b, c;

        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        System.out.println("합 = " + (a+b+c));
        System.out.println("평균 = " + (a+b+c)/3);
    }
}