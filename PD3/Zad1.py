def Nasser_Daniel_ukladL(L,b):
    for i in range(0,len(L)):
        sum=0
        for k in range(0,len(L)):
            if i-1 >= 0 : sum=sum+L[i-1][k]
        x = b[i] - sum
        x = x/L[i][i]
        for k in range (i,len(L)):
            L[k][i] = L[k][i] * x
        print("x",i+1,"=",x)
Macierz = [[1,0,0],[1,2,0],[1,2,1]]
Wolny = [1,3,7]
Nasser_Daniel_ukladL(Macierz,Wolny)