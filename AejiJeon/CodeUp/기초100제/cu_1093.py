# the number of number appearing for each 1 ~ 23

n = input()

nums = input().split()

students = [0] * 23

for num in nums:
    students[int(num) - 1] += 1
for student in students:
    print(student, end = ' ')


