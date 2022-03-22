# The longest common subsequence in Python
from tabulate import tabulate


def lcs_length(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
  
    # declaring the array for storing the dp values
    L = [[0]*(n + 1) for i in range(m + 1)]
    B = [[None]*(n + 1) for i in range(m + 1)]
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
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
                
    print(tabulate(L))
    print(tabulate(B))
    return L, B
