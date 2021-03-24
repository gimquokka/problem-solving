import java.util.Scanner;

public class Quiz05_01 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        char a = input.next().charAt(0);
        char b = input.next().charAt(0);

        System.out.println((int) (a+b)+" "+Math.abs((int) (a-b)));
    }
}
