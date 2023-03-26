def func(matrix: list[list[float]], inv_matrix: list[list[float]], x: list[float], col: int):
    n = len(matrix)
    l = [0] * n
    for i in range(n):
        s = 0
        for j in range(n):
            s += inv_matrix[i][j] * x[i]
        l[i] = s

    if l[col] == 0:
        raise Exception("Matrix is not inversable")

    l_col = l[col]
    l[col] = -1

    l = list(map(lambda x: -1 / l_col * x, l))

    q = []
    for i in range(n):
        q.append([0] * n)

    for i in range(n):
        q[i][i] = 1
        q[i][col] = l[i]

    print(q)

    ans = []
    for i in range(n):
        ans.append([0] * n)

    for i in range(n):
        for j in range(n):
            t1 = q[i][i] * inv_matrix[i][j]
            t2 = q[i][col] * inv_matrix[col][j]
            if i == col:
                t2 = 0
            ans[i][j] = t1 + t2

    return ans

a = [[1, 0, 5],
     [2, 1, 6],
     [3, 4, 0]]

a_inv = [[-24, 20, -5],
         [ 18, 15,  4],
         [  5, -4,  1]]

x = [2, 2, 2]

ans = func(a, a_inv, x, 1)
print(ans)
