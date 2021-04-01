import java.util.ArrayList;

class Solution1 {
    public int[] solution(int[] progresses, int[] speeds) {
        int cnt = 0;
        ArrayList<Integer> ans = new ArrayList();

        for (int i = 0; i < progresses.length; i++) {
            if (progresses[i] < 100) {
                if (cnt > 0) {
                    ans.add(cnt);
                    cnt = 0;
                }
                while (progresses[i] < 100) {
                    for (int j = 0; j < progresses.length; j++) {
                        progresses[j] += speeds[j];
                    }
                }
            }
            cnt++;
        }
        if (cnt > 0) {
            ans.add(cnt);
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
/*
    @Test
    public void 정답() {
        int[] ans = {2, 1};
        int[] progresses = new int[]{93, 30, 55};
        int[] speeds = new int[]{1, 30, 5};
//        assertArrayEquals(new int[]{2, 1}, solution(progresses, speeds));

        ans = new int[]{1, 3, 2};
        progresses = new int[]{95, 90, 99, 99, 80, 99};
        speeds = new int[]{1, 1, 1, 1, 1, 1};
        assertArrayEquals(ans, solution(progresses, speeds));
    }

 */
}

