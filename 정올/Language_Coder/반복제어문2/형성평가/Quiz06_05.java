import java.util.Scanner;

public class Quiz06_05 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int num = 0;
        int even = 0;
        int odd = 0;

        for (int i = 0; i < 10; i++) {
            num = input.nextInt();

            if (num % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
        System.out.println("짝수 : " + even + "개");
        System.out.println("홀수 : " + odd + "개");
    }
}
