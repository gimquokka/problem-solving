1. "네 방향 회전하고도"
=> 회전함수 호출 때마다 turn_time += 1 후, if turn_time == 4로 확인

2. '뒷 방향'
=> nx= x - dx[direction]; ny = y - dy[direction]

3. '방문한 칸'
=> 처음 캐릭터가 놓여진 위치 포함임으로, count = 1부터 시작, 후 (x,y)도 방문처리 꼭!

4. List 마지막 전 원소까지만 얻고 싶다면?
=> d[:-1] (-1이 마지막 원소를 의미함으로)

5. 문자열 함수 정리
    s.count('e')  # arg가 문자열에 몇번 들어가는지 세어 반환
    
    '?'.join(iterable) # iterable의 원소들을 ?를 사이에 넣어 붙여줌. (Ex. 1?2?3?4?5)
    
    s = s.lower() # 모두 소문자로 전환
    s = s.upper() # 모두 대문자로 전환
    
    s.isalpha()  # 문자열의 구성이 알파벳인지 확인하여 True or False 반환
    s.isdigit()  # 문자열의 구성이 숫자인지 확인하여 True or False를 반환
    s.isalnum  # 문자열의 구성이 숫자 혹은 문자인지 확인하여 True or False를 반환 
    
 \# *단, 위 세 함수는 띄어쓰기 등이 포함되어 있으면 False를 Return함*
    
문자열에는 s.sort()가 없다. sorted(s)를 활용해야함
    
    
    
6. list 함수 정리
    l.count(arg) # list 내의 arg의 개수를 반환함

7. import math 사용법 정리
    math.sqrt(arg) # arg의 제곱근을 반환



