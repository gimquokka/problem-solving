import java.util.Scanner;

public class Quiz07_01 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int data = 0;
        int cnt = 0;
        int sum = 0;

        for (int i = 0; i < 20; i++) {
            data = input.nextInt();
            if (data == 0) break;
            sum += data;
            cnt++;
        }

        System.out.println(sum + " " + sum / cnt);
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

