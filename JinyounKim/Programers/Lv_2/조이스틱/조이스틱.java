import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class Solution {
    public int solution(String name) {
        int ans = 0;
        int len = name.length();
        int max_moving = len - 1;
        int next = 0;

        for (int i = 0; i < len; i++) {
            ans += Math.min(name.charAt(i) - 'A', 'Z' - name.charAt(i) + 1);

            next = i + 1;

            while (next < len && name.charAt(next) == 'A') {
                next++;
            }

            if (next == len) {
                max_moving = Math.min(max_moving, i);
            } else {
                max_moving = Math.min(max_moving, i + i + len - next);
            }
        }

        ans += max_moving;
        return ans;
    }
    @Test
    void 정답() {
        String name = "ABAA";
        int ans = 2;
        assertEquals(ans, solution(name));

        name = "JEROEN";
        ans = 56;
        assertEquals(ans, solution(name));

        name = "JAN";
        ans = 23;
        assertEquals(ans, solution(name));

        name = "JAZ";
        ans = 11;
        assertEquals(ans, solution(name));

    }

//    public static void main(String[] args) {
//        System.out.print("abc".charAt(0) - 'b');
//    }
}
