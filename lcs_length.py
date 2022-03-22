# The longest common subsequence in Python

from tabulate import tabulate

def lcs_length(X, Y):

   m, n = len(X), len(Y)
   b, c = [0]*(n+1), [0]*(m+1)

   for i in range(1, m+1):
       for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
               c[j] = 1 + b[j-1]
            #    b[j] = '↖︎'
            elif c[j-1] > b[j]:
                c[j] = c[j-1]
                # b[j] = '↑'
            else:
                c[j] = b[j]
                # b[j] = '←'
       c, b = b, c
   return c, b

X = "ABCBDAB"
Y = "BDCABA"

# X = "10010101"
# Y = "010110110"
# print(lcs_length(X,Y))


def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
  
    # declaring the array for storing the dp values
    L = [[0]*(n + 1) for i in range(m + 1)]
    B = [[None]*(n + 1) for i in range(m + 1)]

    print(tabulate(L))
  
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
# end of function lcs
  
  
# Driver program to test the above function
X = "ABCBDAB"
Y = "BDCABA"
print("Length of LCS is ", lcs(X, Y))
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)



# Function to find the length of the longest common subsequence of substring
# `X[0…m-1]` and `Y[0…n-1]`
def LCSLength(X, Y):
 
    m = len(X)
    n = len(Y)
 
    # lookup table stores solution to already computed subproblems;
    # i.e., `T[i][j]` stores the length of LCS of substring
    # `X[0…i-1]` and `Y[0…j-1]`
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
 
    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if the current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # otherwise, if the current character of `X` and `Y` don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
 
    # LCS will be the last entry in the lookup table
    return T[m][n]
 
 
if __name__ == '__main__':
 
    X = "ABCBDAB"
    Y = "BDCABA"
 
    # print('The length of the LCS is', LCSLength(X, Y))