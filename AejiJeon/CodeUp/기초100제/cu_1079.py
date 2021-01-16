# print input chars continually until 'q' is input

chars = input().split()

for ch in chars:
    print(ch)
    if ch == 'q': break