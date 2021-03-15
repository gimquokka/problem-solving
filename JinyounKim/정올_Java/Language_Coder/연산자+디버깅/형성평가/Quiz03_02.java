import java.util.Scanner;

public class Quiz03_02 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int a, b;
        a = input.nextInt();
        b = input.nextInt();

        System.out.printf("%d / %d = %d...%d", a, b, a/b, a%b);
    }

}
