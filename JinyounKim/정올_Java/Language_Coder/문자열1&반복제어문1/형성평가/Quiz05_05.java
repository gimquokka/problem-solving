import java.util.Scanner;

public class Quiz05_05 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        String a = input.next();
        String b = input.next();
        System.out.println(Math.max(a.length(), b.length()));
    }
}
