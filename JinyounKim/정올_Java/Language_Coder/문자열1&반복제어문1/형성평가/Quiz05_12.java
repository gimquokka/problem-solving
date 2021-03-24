import java.util.Scanner;

public class Quiz05_12 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int l, h;
        char yn;

        do {
            System.out.printf("밑변의 길이 = ");
            l = input.nextInt();

            System.out.printf("높이 = ");
            h = input.nextInt();

            System.out.printf("입력한 삼각형의 없이는 %.1f입니다.", (l * h) / 2.0);

            System.out.printf("\n계속하시겠습니까? ");
            yn = input.next().charAt(0);
        } while (yn == 'Y'|| yn == 'y');
    }
}
