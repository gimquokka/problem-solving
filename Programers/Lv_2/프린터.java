/*
시간 복잡도: O(n^2)

1 2 3 4 1 ,
0
=> 2 , 3 4, 1
=>  4, 1, 1, 2 ,3
=>
1-3 1-4 1-5 4-1 1-2

 */

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int solution(int[] priorities, int location) {
        int ans = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());

        for (int element : priorities) {
            pq.offer(element);
//            System.out.println(pq);
        }

        while (!pq.isEmpty()) {
            for (int i = 0; i < priorities.length; i++) {
                if (pq.peek() == priorities[i]) {
                    pq.poll();
                    ans++;
                    if (i == location) {
                        return ans;
                    }
                }
            }
        }
        return ans;

    }


    @Test
    public void 정답() {
        int[] priorities = new int[] {2, 1, 3, 2};
//        위 아래 둘 다 가능, 아래는 편의상 컴파일러가 지원해주는 convention
        //        int[] priorities = {2, 1, 3, 2};
        Assertions.assertEquals(1, solution(priorities, 2));

        priorities = new int[]{1, 1, 9, 1, 1, 1};
        Assertions.assertEquals(5, solution(priorities, 0));
    }
}
