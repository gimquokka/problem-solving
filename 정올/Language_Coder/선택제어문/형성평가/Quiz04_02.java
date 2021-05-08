import java.util.Scanner;

public class Quiz04_02 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int a = input.nextInt();

        if (a < 0) {
            System.out.println("minus");
        }
        else if (a == 0) {
            System.out.println("zero");
        }
        else {
            System.out.println("plus");
        }
    }
}

