import math;
def funkcja(x):
    return pow(x,2) + x + 3;
def Nasser_Daniel_zloty_podzial(a,b,eps):
    p = (1-math.sqrt(5))/2
    xL = b-p*(b-a)
    xR = a+p*(b-a)
    if b-a < eps : return funkcja((a+b)/2)
    if funkcja(xL) > funkcja(xR) : Nasser_Daniel_zloty_podzial(xL,b,eps)
    if funkcja(xL) < funkcja(xR) : Nasser_Daniel_zloty_podzial(a,xR,eps)