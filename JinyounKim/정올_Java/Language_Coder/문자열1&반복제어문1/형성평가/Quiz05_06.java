import java.util.Scanner;

public class Quiz05_06 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        StringBuffer word = new StringBuffer(input.next());

        while (true) {
            int index = input.nextInt();

            if (index >= word.length()){
                index = word.length();
            }
            word.deleteCharAt(index-1);
            System.out.println(word);

            if (word.length() == 1){
                break;
            }
        }
    }
}