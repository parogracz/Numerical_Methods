
def Nasser_Daniel_ukladU(U,b):
    for i in range(len(U[0])-1,-1,-1):
        sum=0
        for k in range(len(U[0])-1,i,-1):
            sum=sum+U[i][k]
        x=b[i]-sum
        x=x/U[i][i]
        for p in range(i-1,-1,-1):
            U[p][i] = U[p][i] * x
        print("x",i,"=",x)
Macierz = [[1,2,1],[0,2,1],[0,0,1]]
Wektor = [7,3,1]
Nasser_Daniel_ukladU(Macierz,Wektor)