import pylab as plt
import numpy as np
def Nasser_Daniel_MNK(x,y,n):
    A = np.array([[1] for i in range(len(x))])
    for i in range(1,n+1):
        A=np.hstack((A,[[x[j]**i] for j in range(len(x))]))
    At = np.transpose(A)
    Ap = np.dot(At,A)
    Ap = np.linalg.inv(Ap)
    Al = np.dot(At,y)
    Ap = np.dot(Ap,Al)
    print(Ap)
    plt.plot(x,y,'ro')
    X = np.linspace(0,15,100)
    Y = np.copy(X)
    for i in range(100):
        Y[i]=0
        for j in range(len(Ap)):
            Y[i] += Ap[j] * X[i] ** j 
    plt.plot(X,Y)
    plt.show()
x=[3,5,9,10,13,15]
y=[5,5,3,8,10,13]
Nasser_Daniel_MNK(x,y,1)