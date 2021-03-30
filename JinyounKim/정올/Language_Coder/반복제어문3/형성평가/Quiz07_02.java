import java.util.Scanner;

public class Quiz07_02 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int data = 0;

        data = input.nextInt();

        for (int i = 1; i <= 10; i++) {
            if (data*i > 100) break;
            System.out.print(i*data + " ");
            if (data*i % 10 == 0) break;
        }
    }
    /*
    @Test
    public void 정답() {
        InputStream sysInBackup = System.in; // Backup System.in to restore later
        ByteArrayInputStream in = new ByteArrayInputStream("1 2 3 4".getBytes());
        System.setIn(in);
        Scanner


        int[] input = {5, 6, 8, 4, 3, 0};
        for (int i : input) {

        } */
    }

