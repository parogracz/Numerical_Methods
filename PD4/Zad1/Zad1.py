
def Nasser_Daniel_gauss_jordan(A,b):
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i][i] != 0 : mno = A[j][i] / A[i][i];
            for k in range(0,len(A[0])):
                A[j][k] = A[j][k] - (A[i][k] * mno)
            b[j] = b[j] - (b[i] * mno)
    for i in range(len(A)-1,-1,-1):
       for j in range(i-1,-1,-1):
           if A[i][i] != 0 : mno = A[j][i] / A[i][i]
           for k in range(0,len(A[0])):
               A[j][k] = A[j][k] - (A[i][k] * mno)
           b[j] = b[j] - (b[i] * mno)
       b[i] = b[i]/A[i][i]
       print("x",i+1,"=",b[i])

Macierz = [[1,3,5],[2,5,6],[3,1,3]]
Wektor = [8,5,25]
Nasser_Daniel_gauss_jordan(Macierz,Wektor)