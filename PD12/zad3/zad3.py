import math as mh
def feature(x,r):
    return mh.sqrt(r^2-(x-r)^2)

def Nasser_Daniel_hit_or_miss_circle(precision, radius):
    minF = 0
    maxF = radius
    opening = 0
    closing = r*4
    hit=0
    for i in range(0,precision):
        xi = rand.random()*(closing-opening)+opening
        yi = rand.random()*(maxF-minF)+minF
        if feature(xi) > 0 : 
            if feature(xi)>yi: hit += 1
        if feature(xi) < 0 : 
            if feature(xi)>yi: hit -= 1
    return (hit/precision) * (closing - opening) * (maxF - minF)
