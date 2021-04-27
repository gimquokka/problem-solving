n = input()
string = []
num = []

for i in range(len(n)):
    #예외처리로 문자와 숫자를 따로 받는다
    try: num.append(int(n[i]))

    except ValueError:
        string.append(n[i])

num_sum = sum(num)
string.sort()

#출력
for i in string:
    print(i,end='')
print(num_sum)

#sort는 문자를 오름차순할 수도 있다.