public class Quiz09_06 {
    public static void main(String[] args) {
        int[][] arr = new int[5][5];

        arr[0][0] = 1;
        arr[0][2] = 1;
        arr[0][4] = 1;

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (0 <= i - 1) {
                    if (0 <= j - 1) {
                        arr[i][j] += arr[i - 1][j - 1];
                    }
                    if (j + 1 <= 4) {
                        arr[i][j] += arr[i - 1][j + 1];
                    }
                }
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}

