n = int(input())

num = list(map(int , input().split()))

d,m = map(int , input().split())
c= 0

for i in range(0,n-m+1):
    d_ = 0
    for j in range(0,m):
        d_ +=  num[i+j]
    if d_ == d:
        c += 1

print(c)