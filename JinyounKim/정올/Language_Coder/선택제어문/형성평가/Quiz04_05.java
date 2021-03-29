import java.util.Scanner;

public class Quiz04_05 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int a = input.nextInt();

        switch (a) {
            case 2:
                System.out.println("28");
                break;
            case 4: case 6: case 9: case 11:
                System.out.println("30");
                break;
            default:
                System.out.println("31");
        }
    }
}
