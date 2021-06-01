import math as mh
import random as rand

def feature(x):
    return mh.sin(x)

def Nasser_Daniel_hit_or_miss(opening, closing, precision):
    minF = 0
    maxF = 1
    hit=0
    for i in range(0,precision):
        xi = rand.random()*(closing-opening)+opening
        yi = rand.random()*(maxF-minF)+minF
        if feature(xi) > 0 : 
            if feature(xi)>yi: hit += 1
        if feature(xi) < 0 : 
            if feature(xi)>yi: hit -= 1
    return (hit/precision) * (closing - opening) * (maxF - minF)
print(Nasser_Daniel_hit_or_miss(0,mh.pi,20))