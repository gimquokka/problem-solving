def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        # stack에 숫자들이 내림차순으로 쌓이도록
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        # stack[-1] >= num -> num을 stack에 쌓아줌(내림차순 유지)
        # k == 0 -> 나머지 숫자들 그대로 stack에 쌓아줌
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)

    "4177252841"	