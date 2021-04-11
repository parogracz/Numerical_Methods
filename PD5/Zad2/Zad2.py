def Nasser_Daniel_rozklad_LU_doolittle(A):
    U = [[0,0,0],[0,0,0],[0,0,0]]
    L = [[0,0,0],[0,0,0],[0,0,0]]
    x = 0
    for i in range(0, len(A)):
        for j in range(i,len(A)):
            for k in range(0,i):
                x += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - x
            x = 0
        for j in range(i,len(A)):
            if i==j : L[i][i] = 1 
            else : 
                for k in range(0,i):
                  x += L[i][k] * U[k][j]
                L[j][i] = (1/U[i][i])*(A[j][i]-x)
    A = U
    return L
A=[[3,1,2],[6,4,9],[9,4,8]]
print(Nasser_Daniel_rozklad_LU_doolittle(A))
print(A)