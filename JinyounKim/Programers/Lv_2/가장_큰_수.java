import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class Solution {
    /* 실패
    public String solution(int[] numbers) {
        StringBuilder ans = new StringBuilder();
        String[] strArr = new String[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            strArr[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(strArr, (o1, o2) -> {
            int idx1 = 0;
            int idx2 = 0;

            for (int i = 0; i < Math.max(o1.length(), o2.length()); i++) {
                if (o1.charAt(idx1) < o2.charAt(idx2)) return 1;
                else if (o1.charAt(idx1) > o2.charAt(idx2)) return -1;

                if (idx1 < o1.length()-1) idx1++;
                if (idx2 < o2.length()-1) idx2++;
            }
            return 0;
        });


        for (String str : strArr) {
            ans.append(str);
        }

        return ans.toString();
    }
    */
    public String solution(int[] numbers) {
        String ans = "";
        String[] strArr = new String[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            strArr[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(strArr, (o1, o2) -> {
            return (o2 + o1).compareTo(o1 + o2);
        });

        if (strArr[0].charAt(0) == '0') return "0";

        return String.join("", strArr);
    }

    @Test
    void 정답() {
        int[] numbers = {6, 10, 2};
        String ans = "6210";
        assertEquals(ans, solution(numbers));

        numbers = new int[] {3, 30, 34, 5, 9};
        ans = "9534330";
        assertEquals(ans, solution(numbers));
    }
}