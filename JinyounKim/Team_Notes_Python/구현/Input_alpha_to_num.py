# a ~ z를 입력으로 받아 숫자로 전환
char = input()
# ord 함수 이용
num = int(ord(char)) - int(ord('a'))
print(num)
