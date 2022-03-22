from lcs_length import lcs_length


def lcs_print(b, X, i, j):
    # print(i, j, b[i][j])
    if i == 0 or j == 0:
        return

    if b[i][j] == '↖︎':
        lcs_print(b, X, i - 1, j - 1)
        print(X[i-1])
    elif b[i][j] == '↑':
        lcs_print(b, X, i - 1, j)
    else:
        lcs_print(b, X, i, j - 1)


X = "ABCBDAB"
Y = "BDCABA"

l, b = lcs_length(X, Y)

lcs_print(b, X, len(X), len(Y))
