# 그래프
## 그래프를 표현하는 방식
1. 인접 행렬 (Adjacency Matrix)
    - 2차원 배열 사용해서 두 노드에 대한 연결 정보를 저장
2. 인접 리스트 (Adjaceny List)
    - 각 노드마다 연결되어 있는 노드를 리스트로 연결하여 저장

## DFS - 깊이우선, stack
- 동작 방식
    1. 탐색 시작 노드를 스택에 삽입하고 방문처리
    2. 스택의 최상단 노드에 방문하지 않은 인접노드 있으면 해당 노드를 스택에 넣고 방문처리, 그렇지 않다면 스택에서 최상단 노드를 삭제
    3. `2`번의 과정을 반복
- **재귀함수**로 구현 (cpp)
    ~~~cpp
    // 연결 리스트
    void dfs(Node v, Graph g) {
        visit[v] = true;
        cout << v;
        for (auto n : g[v]) {
            if (!visit[v]) {
                dfs(n, g);
            }
        }
    }
    ~~~
- **스택**으로 구현 (cpp)
    ~~~cpp
    // 연결 리스트
    void dfs(Node v, Graph g) {
        stack s;
        s.push(v);
        cout << v;
        visit[v] = true;
        while (!s.isEmpty()) {
            int c_node = s.top();
            s.pop();
            for (int i=0; i<g[v].size(); i++) {
                int n_node = g[v][i];
                if (!visit[n_node]) {
                    cout << n_node;
                    visit[n_node] = true;
                    s.push(c_node);
                    s.push(n_node);
                }
            }
        }
    }
    ~~~
## BFS - 너비우선, queue
- 동작 방식
    1. 탐색 시작 노드를 큐에 삽입, 방문 처리
    2. 큐에서 노드를 꺼내, 해당 노드의 인접 노드 중 방문하지 않는 노드를 모두 큐에 삽입하고 방문처리
    3. `2`를 더 이상 수행할 수 없을 때까지 반복
- **큐**로 구현 (cpp)
    ~~~cpp
    // 연결 리스트
    void dfs(Node v, Graph g) {
        queue q;
        q.push(v);
        cout << v;
        visit[v] = true;
        while (!q.isEmpty()) {
            int c_node = q.front();
            s.pop();
            for (int i=0; i<g[v].size(); i++) {
                int n_node = g[v][i];
                if (!visit[n_node]) {
                    cout << n_node;
                    visit[n_node] = true;
                    q.push(v);
                }
            }
        }
    }
    ~~~