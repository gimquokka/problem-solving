# 2048게임 3
https://codeup.kr/problem.php?id=2050

## Solution
### Sliding Window로 풀었음
1. map에 입력받기
2. 방향에 따라 arr1, arr2, arr3, arr4에 값 분배하기  
<img src="./split.png" width="25%">

3. 중간에 0이 껴있는 경우, 제거하고 한쪽으로 다 밀었음
4. **sliding window**: win_size = 2, 두 값을 비교해서 같으면 앞에 값에 2곱하고, 한칸씩 왼쪽으로 밀기
5. arr값을 다시 map에 합치기
6. Display

## Trouble Shooting
1. arr로 어떻게 나눌까
    - index를 잘 매칭했음 ㅎ.ㅎ
2. sliding을 언제 멈춰야 하나
    - 한바퀴를 다 돌아도 아무런 변화가 없는 경우, 계산이 끝난 것 이므로 `isChange` 플래그를 둬서 loop를 빠져나가게 함
3. 0을 어떻게 제거할까 
    - 지금 생각난건데 그냥 전부다 0말고 -1집어넣어놓고 Display만 0으로 하면되는데 난 멍청이처럼 다섯번째 칸에만 -1이라해놓고 헤헤 나 똑똑하다 이러고 있었네 참나