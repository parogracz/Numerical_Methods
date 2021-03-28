def Zamiana_Wiersza(a,b):
    for i in range(0,len(a)):
        p=a[i]
        a[i]=b[i]
        b[i]=p
def Nasser_Daniel_gauss_pivot(A,b):
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i][i] < A[j][i] : 
                Zamiana_Wiersza(A[i],A[j])
                p=b[i]
                b[i]=b[j]
                b[j]=p
        for j in range(i+1,len(A)):
            if A[i][i] != 0 : mno = A[j][i] / A[i][i];
            for k in range(0,len(A[0])):
                A[j][k] = A[j][k] - (A[i][k] * mno)
            b[j] = b[j] - (b[i] * mno)
        for j in range(i-1,-1,-1):
            if A[i][i] != 0 : mno = A[j][i] / A[i][i]
            for k in range(0,len(A[0])):
               A[j][k] = A[j][k] - (A[i][k] * mno)
            b[j] = b[j] - (b[i] * mno)
    for i in range(0,len(A)):
        b[i] = b[i]/A[i][i]
        print("x",i+1,"=",b[i])

Macierz = [[1,3,5],[2,5,6],[3,1,3]]
Wektor = [8,5,25]
Nasser_Daniel_gauss_pivot(Macierz,Wektor)
