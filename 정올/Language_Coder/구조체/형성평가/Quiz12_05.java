import java.util.Arrays;
import java.util.Scanner;

class ScoreInfo {
    String name;
    int score1, score2, score3, tot_score;

    public ScoreInfo(String name, int score1, int score2, int score3) {
        this.name = name;
        this.score1 = score1;
        this.score2 = score2;
        this.score3 = score3;

        tot_score = score1 + score2 + score3;
    }

    void out() {
        System.out.printf("%s %d %d %d %d", name, score1, score2, score3, tot_score);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        ScoreInfo[] si_arr = new ScoreInfo[n];

        for (int i = 0; i < si_arr.length; i++) {
            si_arr[i] = new ScoreInfo(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt());
        }

        Arrays.sort(si_arr, ((o1, o2) -> o2.tot_score - o1.tot_score));

        for (int i = 0; i < si_arr.length; i++) {
            System.out.printf("%s %d %d %d %d\n",
                    si_arr[i].name, si_arr[i].score1, si_arr[i].score2, si_arr[i].score3, si_arr[i].tot_score);
        }
    }
}