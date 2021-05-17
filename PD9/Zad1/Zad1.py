def Funkcja(x):
    return x*x+x+3
def Nasser_Daniel_bisekcja(a,b,eps):
    c = (a+b)/2
    if Funkcja(c)==0 :
        print("Wynik Dokładny!")
        return c
    if Funkcja(a) * Funkcja(c) < 0 :
        return Nasser_Daniel_bisekcja(c,b,eps)
    if Funkcja(b) * Funkcja(c) < 0 :
        return Nasser_Daniel_bisekcja(a,c,eps)
    if abs(Funkcja(c))<eps : 
        return c

