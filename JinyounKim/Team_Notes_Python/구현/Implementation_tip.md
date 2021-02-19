1. "네 방향 회전하고도"
=> 회전함수 호출 때마다 turn_time += 1 후, if turn_time == 4로 확인

2. '뒷 방향'
=> nx= x - dx[direction]; ny = y - dy[direction]

3. '방문한 칸'
=> 처음 캐릭터가 놓여진 위치 포함임으로, count = 1부터 시작, 후 (x,y)도 방문처리 꼭!

4. 
