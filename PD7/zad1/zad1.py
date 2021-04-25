
def Nasser_Daniel_Lagrange(x,xw,yw,n):
    for wartosc in x:
        suma=0
        for i in range(0,n):
            iloczyn=1
            for j in range(0,n):
                if j!=i : iloczyn*=(wartosc - xw[j]) / ((xw[i] - xw[j]))
            suma+=iloczyn*yw[i]
        print("Dla ",wartosc," = ",suma)

x = [1,2,-1]
xw = [-2,1,4]
yw = [5,3,7]
Nasser_Daniel_Lagrange(x,xw,yw,3)