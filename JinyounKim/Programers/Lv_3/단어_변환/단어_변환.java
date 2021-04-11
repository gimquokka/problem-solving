package 단어_변환;

class Solution {
    // 아래와 같이 그냥 전역변수 선언해주면 됨
    int ans = 51;
    boolean[] visited;

    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];

        dfs(words, begin, target, 0);

        return ans == 51 ? 0 : ans;
    }

    private void dfs(String[] words, String begin, String target, int cnt) {
        if (begin.equals(target)) {
            ans = ans > cnt ? cnt : ans;
        }


        for (int i = 0; i < words.length; i++) {
            if (!visited[i] && check(begin, words[i])) {
                visited[i] = true;
                dfs(words, words[i], target, cnt + 1);
                // 다음 차례의 dfs는 해당 node를 방문해야함으로!
                visited[i] = false;
            }
        }
    }

    private boolean check(String begin, String word) {
        int cnt = 0;

        for (int i = 0; i < word.length(); i++) {
            if (begin.charAt(i) != word.charAt(i)) {
                cnt++;
            }
        }

        return cnt == 1 ? true : false;
    }
}
