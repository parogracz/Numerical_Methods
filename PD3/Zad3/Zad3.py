def Nasser_Daniel_gauss(A,b):
    for i in range(0,len(A)):
        for k in range(i+1,len(A)):
            if A[i][i] != 0 : 
                r = A[k][i] / A[i][i]
            for p in range(i,len(A)):
                A[k][p] = A[k][p] - r * A[i][p]
            b[k] = b[k] - r * b[i] 
            print(A)
            print(b)
            print()

    
    
Macierz = [[1,2,3],[4,5,6],[7,8,9]]
Wektor = [7,3,1]
Nasser_Daniel_gauss(Macierz,Wektor)