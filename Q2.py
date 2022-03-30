def CSCD(s, i, j):
    
    if i == j:
        print ("A"+str(i))
    else:
        print("(")
        CSCD(s, i, s[i-1][j-1])
        CSCD(s, s[i-1][j-1] + 1, j)
        print(")")

s = [[0,1,2,1], [0,0,2,2], [0,0,0,3], [0,0,0,0]]
CSCD(s, 1, 4)