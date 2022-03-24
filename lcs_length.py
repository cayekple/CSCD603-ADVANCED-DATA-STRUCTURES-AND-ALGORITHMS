# coding: utf-8
'''
    Question 1(a)
    
    Computing the length of an LCS
'''


def lcs_length(X, Y):

    m = len(X)
    n = len(Y)

    L = [[0]*(n + 1) for i in range(m + 1)]
    B = [[0]*(n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                B[i][j] = '↖︎'
            elif L[i-1][j] >= L[i][j-1]:
                L[i][j] = L[i-1][j]
                B[i][j] = '↑'
            else:
                L[i][j] = L[i][j-1]
                B[i][j] = '←'

    return L, B
