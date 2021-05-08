import java.util.Scanner;

public class Quiz03_01 {
    public static void main(String[] args){
        int a, b, c, d;
        Scanner input = new Scanner(System.in);
        a = input.nextInt();
        b = input.nextInt();
        c = input.nextInt();
        d = input.nextInt();

        System.out.printf("총점 %d점 \n", a+b+c+d);
        System.out.printf("평균 %d점 \n", (a+b+c+d)/4);
    }
}
