/*
출처: https://velog.io/@hyeon930/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B6%94%EC%84%9D-%ED%8A%B8%EB%9E%98%ED%94%BD-Java
 */
class Solution1 {
    public int solution(String[] lines) {
        int answer = 0;
        int[] startTimes = new int[lines.length];
        int[] endTimes = new int[lines.length];

        getTimes(lines, startTimes, endTimes);

        for(int i = 0 ; i < lines.length ; ++i) {
            int cnt = 0;
            int startOfSection = startTimes[i];
            int endOfSection = startOfSection + 999;

            for(int j = 0 ; j < lines.length ; ++j) {
                if(startTimes[j] >= startOfSection && startTimes[j] <= endOfSection) {
                    cnt++;
                } else if(endTimes[j] >= startOfSection && endTimes[j] <= endOfSection) {
                    cnt++;
                } else if(startTimes[j] <= startOfSection && endTimes[j] >= endOfSection) {
                    cnt++;
                }
            }

            answer = cnt > answer ? cnt : answer;
        }

        for(int i = 0 ; i < lines.length ; ++i) {
            int cnt = 0;
            int startOfSection = endTimes[i];
            int endOfSection = startOfSection + 999;
            // int startOfSection = endTimes[i] - 1000;
            // int endOfSection = endTimes[i];

            for(int j = 0 ; j < lines.length ; ++j) {
                if(startTimes[j] >= startOfSection && startTimes[j] <= endOfSection) {
                    cnt++;
                } else if(endTimes[j] >= startOfSection && endTimes[j] <= endOfSection) {
                    cnt++;
                } else if (startTimes[j] <= startOfSection && endTimes[j] >= endOfSection) {
                    cnt++;
                }
            }

            answer = cnt > answer ? cnt : answer;
        }

        return answer;
    }

    private void getTimes(String[] lines, int[] startTimes, int[] endTimes) {
        for(int i = 0 ; i < lines.length ; ++i) {
            String[] log = lines[i].split(" ");
            String[] responseTime = log[1].split(":");
            int processingTime = (int)(Double.parseDouble(log[2].substring(0, log[2].length() - 1)) * 1000);
            int startTime = 0;
            int endTime = 0;

            endTime += Integer.parseInt(responseTime[0]) * 60 * 60 * 1000;
            endTime += Integer.parseInt(responseTime[1]) * 60 * 1000;
            endTime += (int)(Double.parseDouble(responseTime[2]) * 1000);
            startTime = endTime - processingTime + 1;

            startTimes[i] = startTime;
            endTimes[i] = endTime;
        }
    }
}