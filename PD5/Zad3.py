import math
def Nasser_Daniel_rozklad_cholesky(A):
    L = [[0,0,0],[0,0,0],[0,0,0]]
    x =0
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            for k in range(0,j-1):
                x += L[i][k] * L[j][k]
            if i == j : L[i][i] = math.sqrt(A[i][i] - x)
        for j in range(i, len(A)):
            for k in range(0,j-1):
                x += L[i][k] * L[j][k]
            L[i][j] = (A[i][j] - x) / L[i][i]
    return L
A=[[3,1,2],[6,4,9],[9,4,8]]
print(Nasser_Daniel_rozklad_cholesky(A))
