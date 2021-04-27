n = input()
string = []
num = []

for i in range(len(n)):
    #예외처리로 아스키코드와 숫자를 따로 받는다
    try: num.append(int(n[i]))

    except ValueError:
        string.append(ord(n[i]))

num_sum = sum(num)
string.sort()

for i in range(len(string)):
    string[i] = chr(string[i])

string.append(num_sum)

for i in string:
    print(i,end='')

