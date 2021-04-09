/*
    # 전략
    1. course의 개수 만큼 orders의 원소에서 문자열을 combination으로 추출해낸다.
    2. Set에 넣고, 만약 Set에 이미 있다면 ans array에 추가 시킨다.
    3. 그리고 ans array를 sort하여 반환
 */

import org.junit.jupiter.api.Test;

import java.util.*;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class Solution {
    static List<String> cb;

    public String[] solution(String[] orders, int[] course) {
        // 1. combination(cb)에 dfs를 이용하여 course 원소와 길이 같은 후보 군을 모두 담는다.
        cb = new ArrayList<String>();

        for (String orderString : orders) {
            char[] orderArr = orderString.toCharArray();
            // 알파벳 순으로 정렬
            Arrays.sort(orderArr);

            for (int idx = 0; idx < orderArr.length - 1; idx++) {
                dfs(orderArr, idx, 1, course, String.valueOf(orderArr[idx]));
            }
        }

        // 2. Map을 선언하여 k, v로 담고, key는 keySetArr에 담는다.
        Map<String, Integer> map = new HashMap<>();
        for (String orderName : cb) {
            map.put(orderName, map.getOrDefault(orderName, 0)+1);
        }
        List<String> keySetArr = new ArrayList<>(map.keySet());

        // 3. keySetArr를 v 값이 큰 순으로 담는다.
        Collections.sort(keySetArr, (o1, o2) -> map.get(o2) - map.get(o1));

        // 4. course 원소와 같은 길이와 최대의 v를 가지는 원소를 ansArr에 넣어준다.
        List<String> ansArr = new ArrayList<>();
        int max;
        for (int i = 0; i < course.length; i++) {
            max = 0;
            for (String orderName : keySetArr) {
                if (map.get(orderName) >= 2 && orderName.length() == course[i]) {
                    if (map.get(orderName) >= max) {
                        max = map.get(orderName);
                        ansArr.add(orderName);
                    }
                }
            }
        }
        // 5. ansArr를 정렬한다.
        Collections.sort(ansArr);

        // 6. String[]로 바꾸어 반환한다.
        String[] ans = new String[ansArr.size()];
        ansArr.toArray(ans);
        return ans;

    }

    void dfs(char[] arr, int idx, int length, int[] course, String str) {
        if (Arrays.stream(course).anyMatch(x -> x == length)) {
            cb.add(str);
        }
        for (int i = idx + 1; i < arr.length; i++) {
            dfs(arr, i, length + 1, course, str + String.valueOf(arr[i]));
        }
    }

    @Test
    void 정답() {
        String[] orders = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
        int[] course = {2, 3, 4};
        String[] ans = {"AC", "ACDE", "BCFG", "CDE"};
        assertArrayEquals(ans, solution(orders, course));

        orders = new String[]{"ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"};
        course = new int[]{2, 3, 5};
        ans = new String[]{"ACD", "AD", "ADE", "CD", "XYZ"};
        assertArrayEquals(ans, solution(orders, course));

        orders = new String[]{"XYZ", "XWY", "WXA"};
        course = new int[]{2, 3, 4};
        ans = new String[]{"WX", "XY"};
        assertArrayEquals(ans, solution(orders, course));
    }
}