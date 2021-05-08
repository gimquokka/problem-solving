import java.util.Scanner;

class Main {
    static int N;
    static int[] arr = new int[101];

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        N = input.nextInt();
        dice(1);
    }

    public static void dice(int level) {
        int i;
        if (level > N) {
            output();
            return;
        }
        for (i = 1; i <= 6; i++) {
            System.out.println("level: " + level + " i: " + i);
            arr[level] = i;
            dice(level + 1);
        }
    }

    public static void output() {
        int i;
        for (i = 1; i <= N; i++) {
//            System.out.print(arr[i] + " ");
        }
//        System.out.println();
    }
}
