import java.util.Scanner;

public class Quiz08_06 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char input;
        char[] arr = {'J', 'U', 'N', 'G', 'O', 'L'};
        int findIndex = 0;

        input = sc.next().charAt(0);

        for (int i = 0; i < 6; i++) {
            if (arr[i] == input) {
                System.out.println(i);
                return;
            }
        }
        System.out.println("없는 문자입니다.");
    }
}
