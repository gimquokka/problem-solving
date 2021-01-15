# 21.01.14 cu_2019 ~ cu_2021

cu_2021 : 
input()으로 인한 시간초과 해결 -> sys 모듈의 sys.stdin (훨씬 속도 빠름) import sys 필요
sys.stdin.readline : 한 라인 입력 받을 때 iterable한 객채 for문으로 여러 줄 입력시 마지막 \n까지도 포함
 num = int(input()) -> num = int(sys.stdin.readline())
sys.stdin : 여러 줄 입력 받을 때
for line in sys.stdin: print(line)

sys.stdin은 여러줄을 입력할 때 한줄 씩 처리할 경우 사용 주로 for문에 iterable 객체로 sys.stdin이 들어감.
for문을 종료하고 싶을 경우 Ctrl+Z를 이용. 입력한 line들을 for문 밖에서 하나의 객체로서 다룰 수 없음.

하나의 line만 입력 시 input()이랑 sys.stdin.readline() 기능 동일

for문으로 iteration마다 여러 라인 입력 시 
sys.stdin.readline()으로 입력시에 한 라인의 마지막 \n까지 포함한다. -> 따라서 n번 iteration동안 n보다 더 적은 
line을 입력할 시 나머지 라인은(남은 만큼 엔터 치게되면 반복 종료) 각각 '\n'을 포함하게 된다 
for i in sys.stdin.readline(): 에서도 마지막 \n 포함
input()으로 입력시에 \n 포함 x -> 나머지 라인은 empty string 

int('453\n') : 453

for i in dic : ... for i in dic.key(): ... for i in list(dic): ... 같은 표현

{}은 set이 아니라 dictionary임

# 2021.01.15 cu_2023~2050

cu_2023 : 
“”.join(l) l에는 string, list with strings, tuple with strings

cu_2024 :
삼항연산자 여러 개 중첩 가능 ex) 값1 if 조건1 else 값2 if 조건2 else 값3

cu_2050: 
a==b==c 다 같음
a!=b!=c!=a 다 다름
sys.stdin.readline().strip()  스트링으로 반환
