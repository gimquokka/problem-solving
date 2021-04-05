import java.util.Scanner;
/*

public class Quiz09_10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[][] arr = new String[3][5];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 5; j++) {
                arr[i][j] = sc.next().toLowerCase();
            }
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
*/
public class Quiz09_10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[][] arr = new char[3][5];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 5; j++) {
                arr[i][j] = (char) (sc.next().charAt(0)-'A' + 'a');
            }
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}

