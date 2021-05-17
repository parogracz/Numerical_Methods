def Funkcja(x):
    return x*x+x+3
def Nasser_Daniel_styczne(x,eps):
    if Funkcja(x) == 0:
        print("Wynik Dokładny!")
        return x
    if abs(Funkcja(x)) < eps :
        return x
    xk = x - Funkcja(x)/(2*x+1)
    return Nasser_Daniel_styczne(xk,eps)
    