import java.util.Scanner;

public class Quiz03_07 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        double a, b, c;

        a = input.nextDouble();
        b = input.nextDouble();
        c = input.nextDouble();

        System.out.printf("총점 %d점", (int) a + (int) b + (int) c );
        System.out.printf("\n평균 %d점", (int)((a + b + c)/3));
    }
}
