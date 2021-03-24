import java.util.Scanner;

public class Quiz06_08 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int row = input.nextInt();
        int col = input.nextInt();

        for (int i = 1; i < row+1; i++) {
            for (int j = 1; j < col + 1; j++) {
                System.out.print(i*j + " ");
            }
            System.out.println();
        }

    }
}
