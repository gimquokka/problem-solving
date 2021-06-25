/*
 참고 사이트: https://codevang.tistory.com/316

1. 전략
    1. 시작_시각 기준으로 jobs array를 정렬한다.
    2. 현재 실행_시간 안에 시작_시각이 포함되는 경우 수행_시간 기준으로 pq에 넣고 이 순서대로 반환한다.

2. 정확성 증명
   (1) 1 ~ n번째 수행되는 작업의 수행시간을 rt1~n
   (2) 이들의 시작시간을 s1~n 으로 나타내었을 때 총 처리_시간은

    tot_runtime =
    (rt1) + (rt1+rt2) + (rt1 + rt2 + rt3) + (rt1 + rt2 + rt3 +rt4)... - (s1 + s2 + s3 ...)
    = n*(rt1) + (n-1)*(rt2) + (n-2)(rt3) ... - sigma_1_to_n_(s_i)

 => 즉, 작업 수행 시간이 작은 순서대로 넣어야 최솟값을 가지는 Greedy Property를 가진다.

3. 시간 복잡도
jobs 정렬 + pq 삽입 + pq 인출 + const
= O(nlg(n) + nlg(n) + nlg(n) + C)
= O(nlg(n))
 */

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int solution(int[][] jobs) {
        int ans = 0;
        int idx = 0;
        int end = 0;
        int cnt = 0;
        int[] temp;

        // Sort jobs with 시작 시간 오름차순으로
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        /*
        // Check Sorted well
        for (int[] e : jobs) {
            System.out.printf("(%d, %d) \n", e[0], e[1]);
        }
        */

        // pq를 작업시간에 대하여 오름차순으로 선언
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((o1, o2) -> o1[1] - o2[1]);

        // 작업 수행 시작
        while (cnt < jobs.length) {
            // 1. 현재 end 안에 시작 시각이 포함되는 모든 작업들 pq에 추가
            while (idx < jobs.length && end >= jobs[idx][0]) {
                pq.add(jobs[idx++]);
            }

            // 2. 만약 1.과 같은 작업이 없다면 다음 작업의 시작 시각을 end로 바꿔주기
            if (pq.isEmpty()) {
                end = jobs[idx][0];

            // 3. pq에서 작업 시간이 작은 순서대로 꺼내서 ans와 end 갱신
            } else {
                temp = pq.poll();
                ans += (end + temp[1]) - temp[0];
                end = end + temp[1];
                cnt++;
            }
        }

        // 정답 값 반환: 여기서 int/int => int임으로 소수점 알아서 절사!
        return ans/cnt;
    }

    @Test
    public void 정답() {
        int[][] input = {{0, 3}, {1, 9}, {2, 6}};
        int ans = 9;
        assertEquals(ans, solution(input));

        input = new int[][]{{10, 3}, {1, 11}, {0, 10}};
        ans = 12;
        assertEquals(ans, solution(input));
    }

}
