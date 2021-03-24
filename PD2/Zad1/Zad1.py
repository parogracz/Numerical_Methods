import numpy

a = [[3,1,2],[5,3,7],[7,1,6]]

for i in range(0,len(a) - 1):
    for j in range(i + 1,len(a)):
        if a[i][i] != 0 :
            mno = a[j][i] / a[i][i]
        for k in range(0,len(a[0]) - 1):
            a[j][k] = a[j][k] - (a[i][k] * mno)
print(a)
