

class Solution {
    public int[] solution(int[] prices) {
        int[] ans = new int[prices.length];

        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                ans[i]++;
                if (prices[i] > prices[j]) break;
            }
        }

        return ans;
    }
/*
    @Test
    public void 정답() {
        int[] ans = new int[]{4, 3, 1, 1, 0};
        int[] input = new int[]{1, 2, 3, 2, 3};

        assertArrayEquals(ans, solution(input));
    }

 */
}