import numpy as np
def Nasser_Daniel_Newton_wielowymiarowy(x,y,eps):
    wektor = {0,0}
    wektorH
    while wektor - wektorH <= eps:
        wektorH = wektor
        wektor = wektor - np.dot(np.linalg.inv(x),y)
