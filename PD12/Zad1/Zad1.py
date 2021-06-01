import math as mh

def feature(x):
    return mh.sin(x)

def Nasser_Daniel_Monte_Carlo(opening,closing,precision):
    inc = 1/precision
    sum = 0
    i = 0;
    while i<=1:
        Zn = opening + (closing - opening) * i
        sum += feature(Zn)
        i+=inc
    return ((closing - opening)/precision) * sum

print(Nasser_Daniel_Monte_Carlo(0,mh.pi,100))