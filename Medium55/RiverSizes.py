def riverSizes(matrix):
    """
    Every 1 is visited once: O(wh)
    """
    h, w = len(matrix), len(matrix[0])
    visited = [[False for _ in range(w)] for _ in range(h)]
    river_sizes = []
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and not visited[i][j]:
                river_sizes.append(len_component(matrix, (i, j), visited))
    return river_sizes


def len_component(matrix, n, visited):
    h, w = len(matrix), len(matrix[0])
    len_component = 0
    q = []
    q.append(n)
    while q:
        r, c = q.pop(0)
        if visited[r][c]:
            continue
        visited[r][c] = True
        len_component += 1
        if r + 1 < h and matrix[r + 1][c] == 1 and not visited[r + 1][c]:
            q.append((r + 1, c))
        if c + 1 < w and matrix[r][c + 1] == 1 and not visited[r][c + 1]:
            q.append((r, c + 1))
        if r > 0 and matrix[r - 1][c] == 1 and not visited[r - 1][c]:
            q.append((r - 1, c))
        if c > 0 and matrix[r][c - 1] == 1 and not visited[r][c - 1]:
            q.append((r, c - 1))
    return len_component