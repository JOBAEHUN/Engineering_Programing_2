"""
Created on Mon Mar 17 10:28:03 2025

@author: BaeHun
"""

def multi(v1,v2):
    retList =[]
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

myList =[]
hap, sub = 0,0

myList = multi(100,200)
hap = myList[0]
sub = myList[1]
print("multi()에서돌려준값==> %d, %d" % (hap, sub))
