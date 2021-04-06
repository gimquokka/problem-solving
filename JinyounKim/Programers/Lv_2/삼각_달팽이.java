/*
Credit: https://minhamina.tistory.com/58
 */

class Solution {
    public int[] solution(int n) {
        int[] answer = new int[n * (n + 1) / 2];

        int[][] arr = new int[n][];

        int x = -1, y = 0;
        int num = 1;

        // Initialize arr as ragged array like arr[0].length = 1, arr[1].length = 2 ....
        for (int i = 0; i < arr.length; i++) {
            arr[i] = new int[i + 1];
        }

        // Find out the rule and apply it!
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i; j++) {
                // Case 1: Go down side
                if (i % 3 == 0) {
                    x++;
                // Case 2: Go right side
                } else if (i % 3 == 1) {
                    y++;
                // Case 3: Go Cross side
                } else {
                    x--;
                    y--;
                }
                // Put num to target position
                arr[x][y] = num++;
            }
        }

        // Flatten arr into answer
        int idx = 0;
        for (int[] row : arr) {
            for (int e : row) {
                answer[idx++] = e;
            }
        }

        return answer;
    }

/*
    @Test
    public void 정답() {
        assertArrayEquals(new int[]{1,
                        2, 9,
                        3, 10, 8,
                        4, 5, 6, 7},
                solution(4));
        assertArrayEquals(new int[]{1,
                        2, 12,
                        3, 13, 11,
                        4, 14, 15, 10,
                        5, 6, 7, 8, 9},
                solution(5));
        assertArrayEquals(new int[]{1,
                        2, 15,
                        3, 16, 14,
                        4, 17, 21, 13,
                        5, 18, 19, 20, 12,
                        6, 7, 8, 9, 10, 11},
                solution(6));

    }
 */
}
