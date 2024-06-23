chess = [[0 for x in range(8)] for y in range(8)]

def attack(i, j):
    for k in range(8):
        if chess[i][k]==1 or chess[k][j]==1:
            return True
    for k in range(8):
        for l in range(8):
            if (k+l==i+j) or (k-l==i-j):
                if chess[k][l]==1:
                    return True
    return False

def chess_n_queens(n):
    if n==0:
        return True
    for i in range(8):
        for j in range(8):
            if (not(attack(i,j))) and (chess[i][j]!=1):
                chess[i][j] = 1
                if chess_n_queens(n-1) == True:
                    return True
                chess[i][j] = 0
    return False

chess_n_queens(8);

for i in chess:
    print(i)