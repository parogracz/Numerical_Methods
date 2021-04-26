def Nasser_Daniel_MNK(x,y,n):
    suma = AVGx = AVGy = SQRx = 0
    for i in range(0,n):
        suma += x[i] * y[i]
        AVGx += x[i]
        AVGy += y[i]
        SQRx += x[i] * x[i]
    AVGx /= n
    AVGy /= n
    b = (suma - (n * AVGx * AVGy))/(SQRx-(n*AVGx*AVGx))
    a = AVGy - b * AVGx