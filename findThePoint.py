import math
n = int(input())
list_ = []
for i in range(n):
    px,py,qx,qy = map(int,input().split())
    rx = 2*(qx) - px 
    ry = 2*qy - py
    print(rx,ry) 