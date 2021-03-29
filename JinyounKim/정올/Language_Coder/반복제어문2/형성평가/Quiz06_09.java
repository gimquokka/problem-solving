import java.util.Scanner;

public class Quiz06_09 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                System.out.printf("(%d, %d) ", i, j);
            }
            System.out.println();
        }

    }
}
