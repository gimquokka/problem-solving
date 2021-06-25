def rotate(graph, pos):
    x0, y0, x1, y1 = pos
    temp = graph[x0-1][y1-1]

    # 북쪽
    graph[x0-1][y0:y1] = graph[x0-1][y0-1:y1-1]
    _min = min(min(graph[x0-1][y0:y1]), temp)

    # 서쪽
    for i in range(x0-1, x1-1):
        graph[i][y0-1] = graph[i+1][y0-1]
        _min = min(_min, graph[i][y0-1])

    # 남쪽
    graph[x1-1][y0-1:y1-1] = graph[x1-1][y0:y1]
    _min = min(_min, min(graph[x1-1][y0-1:y1-1]))

    # 동쪽
    for i in range(x1-1, x0, -1):
        # print(i)
        graph[i][y1-1] = graph[i-1][y1-1]
        _min = min(_min, graph[i][y1-1])

    graph[x0][y1-1] = temp

    return _min


def solution(rows, columns, queries):
    answer = []
    graph = [[i + columns*j for i in range(1, columns+1)] for j in range(rows)]

    for pos in queries:
        answer.append(rotate(graph, pos))
        # for row in graph:
        #     print(*row)
        # print()
    return answer


# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# print(solution(6, 6, queries))

queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
print(solution(3, 3, queries))

# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# print(solution(6, 6, queries))
