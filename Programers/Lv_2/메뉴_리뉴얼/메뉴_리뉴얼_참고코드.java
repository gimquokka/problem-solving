/*
참고 링크: https://velog.io/@hammii/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%94%EB%89%B4-%EB%A6%AC%EB%89%B4%EC%96%BC-java-2021-KAKAO-BLIND-RECRUITMENT
    # 알고리즘
    1. 한 order씩 char array로 변환 -> 오름차순 정렬
    2. 한 글자씩 차례대로 선택하면서, course 하나씩 바꿔가면서 dfs 호출
    3. dfs에서 length가 course와 같다면(하나의 경우가 만들어졌을 때) 조합 배열에 추가
    4. 조합 배열에서 많이 나타나는 순서대로 내림차순 정렬
    5. 문자열의 길이가 같은 조합 중 가장 많이 나타난 조합 찾기

    # 배워야 하는 것
    1. private static className refName
    2. 자료구조들
        (1) List<T>
        (2) ArrayList
        (3) Map<K, V>
        (4) HashMap<K, V>
        (5) Arrays.sort() vs Collections.sort()
        (6) Collection interface
 */

import java.util.*;

class SolutionRef {
    private static List<String> combination;

    public String[] solution(String[] orders, int[] course) {
        String[] answer;
        combination = new ArrayList<>();

        for (int i = 0; i < orders.length; i++) {   // 한 주문당 모든 조합 구하기
            char[] orders_char = orders[i].toCharArray();
            Arrays.sort(orders_char);

            for (int index = 0; index < orders_char.length - 1; index++) {  // 차례대로 한글자씩 선택 후
                  /*
                  // for 문을 대체할 수 있음!
                for (int j = 0; j < course.length; j++) {
                    dfs(orders_char, index, 1, course[j], String.valueOf(orders_char[index]));
                }
                   */
                // course 에 있는 모든 경우
                    dfs(orders_char, index, 1, course, String.valueOf(orders_char[index]));

            }
        }

        Map<String, Integer> map = new HashMap<>();
        for (String key : combination) {
            map.put(key, map.getOrDefault(key, 0) + 1);
        }
        List<String> keySetList = new ArrayList<>(map.keySet());
        // 아래 두 개가 같은 코드!
        // Collections.sort(keySetList, (o1, o2) -> (map.get(o2).compareTo(map.get(o1))));
        Collections.sort(keySetList, (o1, o2) -> (map.get(o2)-map.get(o1)));

        List<String> ansList = new ArrayList<>();
        for (int targetLength: course) {
            int max_value = 0;

            for (String key : keySetList) {
                if (map.get(key) >= 2 && key.length() == targetLength) {
                    if (map.get(key) >= max_value) {
                        ansList.add(key);
                        max_value = map.get(key);
                    }
                }
            }
        }
        Collections.sort(ansList);
        answer = new String[ansList.size()];
        ansList.toArray(answer);

        return answer;
    }

    public static void dfs(char[] arr, int idx, int length, int[] course, String str) {
        if (Arrays.stream(course).anyMatch(x -> x == length)) {    // 경우의 수 추가
            combination.add(str);
        }

        for (int i = idx + 1; i < arr.length; i++) {
            dfs(arr, i, length + 1, course, str + arr[i]);
        }
    }
}