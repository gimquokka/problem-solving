import java.util.Optional;
import java.util.Scanner;
import java.util.stream.Stream;

public class Quiz07_09 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        Optional<String> init = Stream.generate(() -> " ").limit(2 * n - 1).reduce((a, b) -> a + b);
        char[] charArray = init.get().toCharArray();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2 * i + 1; j += 2) {
                charArray[j] = '#';
            }
            System.out.println(String.valueOf(charArray));
        }

        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < 2 * i + 1; j += 2) {
                charArray[j] = ' ';
            }
            System.out.println(String.valueOf(charArray));
        }
    }
}


