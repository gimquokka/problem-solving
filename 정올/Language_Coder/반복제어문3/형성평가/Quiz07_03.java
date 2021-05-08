import java.util.Optional;
import java.util.Scanner;
import java.util.stream.Stream;

public class Quiz07_03 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = 0;

        n = input.nextInt();

        for (int i = 1; i <= 2 * n - 1; i++) {
            if (i > n) {
                Optional<String> result = Stream.generate(() -> "*").limit(2 * n - i).reduce((a, b) -> a + b);
                System.out.println(result.get());
                continue;
            }
            Optional<String> result = Stream.generate(() -> "*").limit(i).reduce((a, b) -> a + b);
            System.out.println(result.get());
        }
    }

}

