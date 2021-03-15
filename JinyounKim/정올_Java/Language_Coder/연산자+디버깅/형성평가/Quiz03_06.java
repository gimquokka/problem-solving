import java.util.Scanner;

public class Quiz03_06 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int a, b, c;
        a = input.nextInt();
        b = input.nextInt();
        c = input.nextInt();
        System.out.printf("%.1f점", (a+b+c)/3.0);
    }
}
