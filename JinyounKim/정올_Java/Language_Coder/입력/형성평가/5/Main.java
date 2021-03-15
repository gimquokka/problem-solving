import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        Double input;
        System.out.print("몇 야드인지 입력하시오. ");
        input = sc.nextDouble();
        System.out.printf("%.1f야드 = %.1fcm", input, input*91.44);
    }
}