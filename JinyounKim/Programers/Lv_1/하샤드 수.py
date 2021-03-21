def solution(phone_number):
    ans = "*"*(len(phone_number)-4) + "".join(phone_number[-4:])
    return ans

print(solution("01033334444"))
print(solution("010333341234"))