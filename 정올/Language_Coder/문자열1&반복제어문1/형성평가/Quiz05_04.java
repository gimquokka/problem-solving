import java.util.Scanner;

public class Quiz05_04 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        String word = input.next();
        char c = input.next().charAt(0);
        int index = word.indexOf(c);
        if (index == -1) {
            System.out.println("No");
        }
        else {
            System.out.println(index);
        }
    }
}
