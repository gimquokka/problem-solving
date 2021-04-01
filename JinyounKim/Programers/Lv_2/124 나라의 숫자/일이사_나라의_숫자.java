import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Solution {
    /*
    public String solution(long n) {
//        System.out.println(resursion(1));
        return resursion(n);
    }

    public String resursion(long n) {
        if (n == 0) {
            return "";
        }

        if (n % 3 == 0) {
            return resursion(n / 3 - 1) + "4";
        } else if (n % 3 == 1) {
            return resursion(n / 3) + "1";
        } else {
            return resursion(n / 3) + "2";
        }
    }
     */
    public String solution(int n) {
        String[] num = {"4","1","2"};
        String answer = "";

        while(n > 0){
            answer = num[n % 3] + answer;
            n = (n - 1) / 3;
        }
        return answer;
    }

    @Test
    public void 정답() {
//        assertEquals("1", solution(1));
//        assertEquals("2", solution(2));
//        assertEquals("4", solution(3));
//        assertEquals("11", solution(4));
//        assertEquals("12", solution(5));
//        assertEquals("14", solution(6));
//        assertEquals("21", solution(7));
//        assertEquals("22", solution(8));
        assertEquals("24", solution(9));
        assertEquals("41", solution(10));
    }

}
