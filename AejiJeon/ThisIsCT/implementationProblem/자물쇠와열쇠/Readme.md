# 효율적인 풀이
lock 늘린 후-> key를 차례대로 겹치면서 더해준다 -> 자물쇠 부분의 모든 값이 1이라면 True(0인 부분은 홈과 홈이 만났을 때, 2인 부분은 돌기와 돌기가 만났을 때, 1인 부분은 홈과 돌기가 만났을 때)
해설에서는 자물쇠 리스트 크기를 3배이상 늘려서 푸는데 정확하게는 (2m+n-2)x(2m+n-2) 배열로 늘리는게 맞다.
2차원 리스트(nxm) 90도 회전하는 ftn은 외워두면 좋다.

# 궁금한 점
What type of binging is python?
maybe static binding without copy module?