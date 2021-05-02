import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Solution {
    public int solution(String[] lines) {
        int ans = 0;
        int[] startInterval = new int[lines.length];
        int[] endInterval = new int[lines.length];

        getInterval(lines, startInterval, endInterval);

        int startOverlapInterval = findMaxOverlapInterval(startInterval, endInterval, startInterval);
        int endOverlapInterval = findMaxOverlapInterval(startInterval, endInterval, endInterval);

        ans = startOverlapInterval > endOverlapInterval ? startOverlapInterval : endOverlapInterval;

        return ans;
    }

    private int findMaxOverlapInterval(int[] startInterval, int[] endInterval, int[] Interval) {
        int maxOverlap = 0;

        for (int i = 0; i < Interval.length; i++) {
            int cnt = 0;
            int startTime = Interval[i];
            int endTime = Interval[i] + 999;

            for (int j = 0; j < startInterval.length; j++) {
                if (startTime <= startInterval[j] && startInterval[j] <= endTime) {
                    cnt++;
                } else if (startTime <= endInterval[j] && endInterval[j] <= endTime) {
                    cnt++;
                } else if (startInterval[j] <= startTime && endTime <= endInterval[j]) {
                    cnt++;
                }
            }

            maxOverlap = maxOverlap > cnt? maxOverlap: cnt;
        }

        return maxOverlap;
    }

    private static void getInterval(String[] lines, int[] startInterval, int[] endInterval) {
        for (int i = 0; i < lines.length; i++) {
            String[] log = lines[i].split(" ");
            String[] responseTime = log[1].split(":");

            int processingTime = (int) (Double.parseDouble(log[2].substring(0, log[2].length()-1)) * 1000);
            int startTime = 0;
            int endTime = 0;

            endTime += Integer.parseInt(responseTime[0]) * 60 * 60 * 1000;
            endTime += Integer.parseInt(responseTime[1]) * 60 * 1000;
            endTime += Double.parseDouble(responseTime[2]) * 1000;

            startTime = endTime - processingTime + 1;

            startInterval[i] = startTime;
            endInterval[i] = endTime;
        }
    }

    public static void main(String[] args) {
        String[] lines = {"2016-09-15 00:00:00.000 3s"};
        int[] startInterval = new int[lines.length];
        int[] endInterval = new int[lines.length];
        getInterval(lines, startInterval, endInterval);
        System.out.println("startInterval : " + startInterval[0]);
        System.out.println("endInterval : " + endInterval[0]);
    }


    @Test
    void 정답() {
        String[] lines = {"2016-09-15 00:00:00.000 3s"};
        int ans = 1;
        assertEquals(ans, solution(lines));

        lines = new String[] {"2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"};
        ans = 7;
        assertEquals(ans, solution(lines));

        lines = new String[]{"2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"};
        ans = 1;
        assertEquals(ans, solution(lines));

    }
}
