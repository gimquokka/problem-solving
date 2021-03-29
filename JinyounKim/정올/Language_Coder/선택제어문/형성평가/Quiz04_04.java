import java.util.Scanner;

public class Quiz04_04 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("1. 개");
        System.out.println("2. 고양이");
        System.out.println("3. 병아리");
        System.out.print("영어로 알고 싶은 번호를 입력하세요. ");
//        System.out.print("Number? ");

        int num = input.nextInt();

        switch (num) {
            case 1:
                System.out.println("dog");
                break;
            case 2:
                System.out.println("cat");
                break;
            case 3:
                System.out.println("chick");
                break;
            default:
                System.out.println("I don't know.");
        }
    }
}
