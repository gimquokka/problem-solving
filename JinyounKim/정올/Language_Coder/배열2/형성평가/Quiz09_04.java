public class Quiz09_04 {
    public static void main(String[] args) {
        int[][] arr = {{3, 5, 9}, {2, 11, 5}, {8, 30, 10}, {22, 5, 1}};
        int sum = 0;
        for (int i = 0; i < 4; i++) {
            System.out.printf("%d %d %d\n", arr[i][0], arr[i][1], arr[i][2]);
            sum += arr[i][0] + arr[i][1] + arr[i][2];
        }
        System.out.println(sum);
    }
}

