# print num of input element by array with reverse order
n = int(input())
input_array = list(map(int, input().split()))

# reverse array
input_array.reverse()

# print array with unpacking array
print(*input_array, sep=' ')