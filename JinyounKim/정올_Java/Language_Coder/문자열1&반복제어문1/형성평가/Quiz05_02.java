import java.util.Scanner;

public class Quiz05_02 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        String word = input.next();

        System.out.println(word.substring(0, 5));
    }
}
