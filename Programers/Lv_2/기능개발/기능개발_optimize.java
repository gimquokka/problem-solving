import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class Solution {
    public static int[] solution(int[] progresses, int[] speeds) {
        int day = 0;
        int[] daysOfEnd = new int[100];

        for (int i = 0; i < progresses.length; i++) {
            while (progresses[i] + (day * speeds[i]) < 100) {
                day++;
            }
            daysOfEnd[day]++;
        }
        return Arrays.stream(daysOfEnd).filter(i -> i != 0).toArray();
    }
}

class TestAnswer {
    @Test
    public void 정답() {
        int[] ans = {2, 1};
        int[] progresses = new int[]{93, 30, 55};
        int[] speeds = new int[]{1, 30, 5};
        assertArrayEquals(new int[]{2, 1}, Solution.solution(progresses, speeds));

        ans = new int[]{1, 3, 2};
        progresses = new int[]{95, 90, 99, 99, 80, 99};
        speeds = new int[]{1, 1, 1, 1, 1, 1};
        assertArrayEquals(ans, Solution.solution(progresses, speeds));
    }
}

