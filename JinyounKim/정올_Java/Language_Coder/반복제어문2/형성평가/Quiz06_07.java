import java.util.Scanner;

public class Quiz06_07 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        for (int i = 1; i < 11; i++) {
            System.out.print(i*n + " ");
        }

    }
}
