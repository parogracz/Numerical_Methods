def funkcja(x):
    return x**2 + 2 * x - 1;
def Nasser_Daniel_trapezy(a,b,n):
    P = (b-a)/(n-1)
    suma = 0
    i=a
    while i<=b:
        suma += (funkcja(i) + funkcja(i+P)) * P/2
        i+=P
    return suma
print(Nasser_Daniel_trapezy(-1,3,100))
