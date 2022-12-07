from math import * 
from itertools import *

n = int(input("n"))
count = 0
maxv = floor(sqrt(n))
list1 = []
list2 = []
for i in range(maxv+1):
    list1.append(i)
    list2.append(i)
    i += 1
    
perms = list(product(list1, list2))
print(perms)
for i in range(len(perms)):
    a = perms[i:0]
    b = perms[i:1]
    if a ** 2 + b ** 2 < n:
        count += 1
    i += 1

print(count)


