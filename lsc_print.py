# coding: utf-8

'''
    Question 1(b)

    Using the recursive procedure to prints out an LCS of X and Y in the proper, 
    forward order.
'''

from lcs_length import lcs_length

def lcs_print(b, X, i, j):

    if i == 0 or j == 0:
        return
    if b[i][j] == '↖︎':
        lcs_print(b, X, i - 1, j - 1)
        print(X[i-1])
    elif b[i][j] == '↑':
        lcs_print(b, X, i - 1, j)
    else:
        lcs_print(b, X, i, j - 1)


X = "10010101"
Y = "010110110"

l, b = lcs_length(X, Y)

lcs_print(b, X, len(X), len(Y))
