import java.util.Scanner;

public class Quiz06_03 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int multiple = 5, sum = 0;
        int n = input.nextInt();

        while (multiple <= n) {
            sum += multiple;
            multiple += 5;
        }

        System.out.println(sum);
    }
}
