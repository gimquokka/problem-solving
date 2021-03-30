import java.util.Optional;
import java.util.Scanner;
import java.util.stream.Stream;

public class Quiz07_10 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        char num = '1';
        int n = input.nextInt();

        for (int i = 0; i < n; i++) {
            Optional<String> init = Stream.generate(() -> " ").limit(2 * n - 1).reduce((a, b) -> a + b);
            char[] charArray = init.get().toCharArray();
            for (int j = 0; j < 2 * n; j += 2) {
                if (num > '9') {
                    num -= 10;
                }
                charArray[j] = num;
                num += 2;
            }
            System.out.println(String.valueOf(charArray));
        }
    }
}


