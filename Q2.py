def CSCD(s, i, j):
    if i == j:
        print ("A")
    else:
        print("(")
        CSCD(s, i, s[i][j])
        CSCD(s, s[i][j], j)
        print(")")

s = []
CSCD(s, 1,6)