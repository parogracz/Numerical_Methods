def Funkcja(x):
    return x*x+x+3
def Nasser_Daniel_sieczne(x1,x2,eps):
    if Funkcja(x2) == 0:
        print("Wynik Dokładny!")
        return x
    if abs(Funkcja(x2)) < eps :
        return x
    xk = x2 - (x2-x1)/(Funkcja(x2)-Funkcja(x1))
    return Nasser_Daniel_sieczne(x2,xk,eps)
