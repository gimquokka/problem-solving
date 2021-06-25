package 단어_변환;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Solution1 {

    static int ans = 51;

    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        if (Arrays.stream(words).anyMatch(x -> x == target)) {
            return 0;
        }

        dfs(words, begin, target, 0);
        return ans == 51? 0: ans;
    }

    public static boolean oneDiff(String a, String b) {
        int cnt = 0;

        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                cnt++;
            }
        }

        return cnt == 1 ? true : false;
    }

    public static void dfs(String[] word, String begin, String target, int cnt) {
        if (begin.equals(target)) { // 대박...
//            System.out.println("check");
            if (cnt < ans) {
//                System.out.println(begin + target);
                ans = cnt;
                return;
            }
        } else if (cnt > word.length) {
            return;
        }

        for (int i = 0; i < word.length; i++) {
            if (oneDiff(begin, word[i])) {
                String[] newWord = new String[word.length - 1];
//                System.out.println(word.length - 1);
                for (int j = 0; j < word.length; j++) {
                    if (j >= i && j !=0) {
//                        System.out.println(i + " " +j);
                        newWord[j - 1] = word[j];
                    } else {
                        newWord[j] = word[j];
                    }
                }

                dfs(word, word[i], target, cnt + 1);
//                System.out.println("begin: " + word[i] + " target: " + target);
            }
        }
    }

    @Test
    public void 정답() {
        String begin = new String("hit");
        String target = new String("cog");
        String[] words = {"hot", "dot", "dog", "lot", "log", "cog"};
        assertEquals(4, solution(begin, target, words));

        begin = "hit";
        target = "cog";
        words = new String[]{"hot", "dot", "dog", "lot", "log"};
        ans = 0;
        assertEquals(0, solution(begin, target, words));

    }

}