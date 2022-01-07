class Para(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def zamiana(self):
        self.a, self.b = self.b, self.a


def zamiana1(x,y):
    a,b = y,x
    print(a,b)
def zamiana2(x,y):
    global a,b 
    a,b = y,x
    print(a,b)
def zamiana3(x,y):
    return y,x

from collections import deque

A = deque([4,5,67,3,2,4,5,6])
print(list(A))
A.append(99)
print(list(A))
print(sorted(A))
A.pop()
A.popleft()
print(list(A))
# zamiana1(4,3)
# zamiana2(4,3)
# pierwsza, druga = zamiana3(4,3)
# print(pierwsza, druga)
# para = Para(2,3)
# para.zamiana()
# print(para.a," oraz ",para.b)
# a = [1,6,3,2,8,7,4,3,6,4,5,3,2,1,5,6]
# a.sort()
# print(sorted(a))
# print(a)