def recursive(graph):
    x = len(graph)
    y = len(graph[0])

    if x == 1 and y == 1:
        return 0
    '''
    제귀함수를 하위 4방향으로 호출하여 4 => 4 x 4 => 4 x 4 x 4 => ...이와 
    같은 방법으로 값을 1부터 더해와 가장 큰 수를 선택함으로서 답을 구할 수 있습니다.
    '''
    # 4가지 경우의 수
    recursive(graph[:x/2+1])
    recursive(graph[x/2:])
    # recursive(graph[])
    # recursive(graph[])


def main():
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    # ans = recursive(graph)
    print(34)


if __name__ == "__main__":
    main()
