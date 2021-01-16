# octal -> decimal
#직접 구하기
oct = input()
l = len(oct)-1
dec = 0
for dig in oct:
    dec += int(dig)*pow(8,l)
    l -= 1
print(dec)

#파이썬 내장함수
"""
dec = input()
oct = int(dec, 8)
print(oct)
"""