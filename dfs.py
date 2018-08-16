def dfs(graph):
    parent = [None] * len(graph[0])
    count_pairings = 0
    for i in range(len(graph[0])):
        visited = [False] * len(graph[0])
        if dfs_visit(graph, i, visited, parent):
            count_pairings += 1
    return len(graph[0]) - 2 *(count_pairings / 2)

def dfs_visit(graph, i, visited, parent):
    for u in range(len(graph[i])):
        if graph[i][u] and visited[u] == False:
            visited[i] = True
            if parent[u] == None or dfs_visit(graph, parent[u], visited, parent):
                parent[u] = i
                return True
    return False

