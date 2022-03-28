import math
def XXO(p):
    n = len(p)-1
    m = [[0] * n for i in range(n)]
    s = [[0] * n for i in range(n)]

    for i in range(1, n):
        m[i][i] = 0
    
    for l in range(2, n):
        
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = math.inf
            print(l, n - l, i, j, m[i][j])
            for k in range(i, j - 1):
                print(i, k, m[i][k], m[k + 1][j], p[i - 1] * p[k] * p[j])
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

p = [24, 30, 45, 60, 15]

XXO(p)