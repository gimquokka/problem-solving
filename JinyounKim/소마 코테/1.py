def main():
    data = list(input().split())
    n = int(input())
    graph = []
    tmp = []
    for i in range(n):
        a, b = input().split()
        flag = False
        for last in graph:
            if last[-1] == a:
                last.append(b)
                flag = True
        if not flag:
            graph.append([a, b])
            tmp.append([a, b])
        # GG TT
    print(graph)


if __name__ == "__main__":
    main()
