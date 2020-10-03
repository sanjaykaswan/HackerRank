import math
import os
import random
import re
import sys

n,m = map(int , input().split())
list_ =[]
ans = []
a = list(map(int , input().split()))
b = list(map(int , input().split()))

for i in range(max(a),min(b)+1):
    k = 0
    for j in a:
        if i%j == 0:
            k += 1
    if k == n:
        list_.append(i)
    else:
        pass

for l in list_:
    p = 0
    for o in b:
        if o%l == 0:
            p += 1
    if p == m:
        ans.append(l)

print(len(ans))