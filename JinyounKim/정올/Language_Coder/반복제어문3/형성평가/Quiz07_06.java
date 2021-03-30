import java.util.Optional;
import java.util.Scanner;
import java.util.stream.Stream;

public class Quiz07_06 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        for (int i = 0; i < n; i++) {
            Optional<String> init = Stream.generate(() -> " ").limit(2 * n - 1).reduce((a, b) -> a + b);
            String[] charArray = init.get().split("");
//            System.out.println(charArray.length);
            int num = 1;
            for (int j = (2 * n - 1) - 2 * i; j < 2 * n; j += 2) {
                charArray[j - 1] = String.valueOf(num);
                num += 1;
            }
//            String row = String.valueOf(charArray);
            System.out.println(String.join("", charArray));
        }

    }
}


