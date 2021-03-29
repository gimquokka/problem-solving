/*
- 문제해결 전략
1. w x h 인 사각형은 대각선을 그으면 (w/gcd)*(h/gcd)인 작은 직사각형으로 나누어짐
2. w x h 인 사각형의 대각선을 그었을 때 멀쩡한 사각형의 개수는
    멀쩡한 사각형의 개수= w*h - (w+h+1)

- 주의!
1. w*h가 int의 범위를 넘어갈 수 있음으로, 결과 값은 long로 받아야 함
    => long = int * int이 아니라 long = long*int로 수행해줘야함
    => int * int => int이기 때문에 overflow가 났을때 값이 씹힘
 */

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.math.BigInteger;
class Solution {
    public long solution(long w, long h) {
        // 1. Get GCD of w, h
        int gcd = BigInteger.valueOf(w).gcd(BigInteger.valueOf(h)).intValue();
//        System.out.println(gcd);

        // 2. Get num of fine rectangular
        return w * h - (w / gcd + h / gcd - 1) * gcd;
    }

    @Test
    public void 정답() {
        assertEquals(80, solution(8, 12));
        assertEquals(80, solution(12, 8));
        assertEquals(12, solution(4, 4));
    }
}

