

class Solution {
    public static String solution(String number, int k) {
        // StringBuilder를 쓰는 것이 char[] 보다 더 빠르고 간편함
        //        StringBuilder ans = new StringBuilder();
        char[] ans = new char[number.length() - k];

        int left = 0;
        int max;
        char tempChar;

        for (int i = 0; i < number.length() - k; i++) {
            max = -1;
            for (int j = left; j <= k + i; j++) {
                tempChar = number.charAt(j);
                if (max < tempChar - '0') {
                    max = tempChar - '0';
                    left = j + 1;
                }
            }
            ans[i]= (char)(max+'0');
        }

//        return ans.toString();
        return String.valueOf(ans);
    }
/*
    @Test
    public void 정답() {
        assertEquals("94", solution("1924", 2));
        assertEquals("3234", solution("1231234", 3));
        assertEquals("775841", solution("4177252841", 4));
    }

*/
}
