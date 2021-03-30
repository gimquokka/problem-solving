import java.util.Optional;
import java.util.Scanner;
import java.util.stream.Stream;

public class Quiz07_07 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        char alpabet = 'A';
        int num = 0;

        Optional<String> init = Stream.generate(() -> " ").limit(2 * n - 1).reduce((a, b) -> a + b);
        String[] charArray = init.get().split("");

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2*(n-i); j += 2) {
                charArray[j] = String.valueOf(alpabet);
                alpabet++;
            }
            for (int j = 2 * (n - i); j < 2 * n; j += 2) {
                charArray[j] = String.valueOf(num);
                num += 1;
            }
            System.out.println(String.join("",charArray));
        }
    }
}


