def MacierzL(A):
    for i in range(len(A)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if A[i][i] != 0 : mno = A[j][i] / A[i][i]
            for k in range(0,len(A[0])):
                A[j][k] = A[j][k] - (A[i][k] * mno)
        for j in range(0,len(A[0])):
            div = A[i][i]
            A[i][j] = A[i][j] / div
    print(A)
def MacierzU(A):
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i][i] != 0 : mno = A[j][i] / A[i][i]
            for k in range(0,len(A[0])):
                A[j][k] = A[j][k] - (A[i][k] * mno)
    print(A)
Macierz=[[1,3,5],[2,3,6],[4,7,10]]
MacierzL(Macierz)
Macierz=[[1,3,5],[2,3,6],[4,7,10]]
MacierzU(Macierz)