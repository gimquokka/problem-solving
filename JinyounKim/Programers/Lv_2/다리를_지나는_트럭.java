/*
참조코드: https://rooted.tistory.com/22
개선점
if else 구문 제거
 */

import java.util.LinkedList;
import java.util.Queue;


class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int ans = 0;
        int sum = 0;

        Queue<Integer> q = new LinkedList<>();

        for (int w : truck_weights) {
            while (true) {
                if (q.size() == bridge_length) {
                    sum -= q.poll();
                } else if (w + sum <= weight) {
                    sum += w;
                    q.offer(w);
                    ans++;
                    break;
                } else {
                    q.offer(0);
                    ans++;
                }
            }
        }

        return ans + bridge_length;
    }
    /*
    @Test
    void test() {
        int bridge_length = 2;
        int weight = 10;
        int[] truck_weight = {7, 4, 5, 6};
//        assertEquals(8, solution(bridge_length, weight, truck_weight));

        bridge_length = 100;
        weight = 100;
        truck_weight = new int[]{10};
        assertEquals(101, solution(bridge_length, weight, truck_weight));

        bridge_length = 100;
        weight = 100;
        truck_weight = new int[]{10,10,10,10,10,10,10,10,10,10};
        assertEquals(110, solution(bridge_length, weight, truck_weight));

    }
     */
}
