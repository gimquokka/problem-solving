# print alphabets from a to an input char

ch = input()

start = ord('a')
end = ord(ch)

for elem in range(start, end + 1):
    print(chr(elem), end = ' ')

