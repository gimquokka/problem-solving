import java.util.Scanner;

public class Quiz05_03 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        String word = input.next();

        for(int i = 0; i < word.length(); i++) {
            if ('a' <= word.charAt(i) && word.charAt(i) <= 'z') {
                System.out.print(word.charAt(i));
            }
            else if ('0' <= word.charAt(i) && word.charAt(i) <= '9') {
                System.out.print(word.charAt(i));
            }
            else if ('A' <= word.charAt(i) && word.charAt(i) <= 'Z') {
                System.out.print((char) (word.charAt(i) + 32));
            }
        }
    }
}
