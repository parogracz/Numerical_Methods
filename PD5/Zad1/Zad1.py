def Nasser_Daniel_rozklad_LU_gauss(A):
    B = [[1,1,1],[1,1,1],[1,1,1]]
    for i in range(0,len(A[0])):
        B[0][i] = A[0][i]
    for i in range(0, len(A)):
        for j in range(i+1,len(A)):
            if A[i][i] != 0 : x = A[j][i] / A[i][i]
            else: x
            for k in range(i,len(A[0])):
                B[j][k] = A[j][k] - (x * A[i][k])
    for i in range(len(A)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if A[i][i] != 0 : x = A[j][i] / A[i][i]
            else: x
            for k in range(i,len(A[0])):
                A[j][k] = A[j][k] - (x * A[i][k])
        for k in range(0,len(A[0])):
            A[i][k] = A[i][k] / A[i][i]
    return B

A=[[3,1,2],[6,4,9],[9,4,8]]
#Nasser_Daniel_rozklad_LU_gauss(A)
print(Nasser_Daniel_rozklad_LU_gauss(A))
print(A)
