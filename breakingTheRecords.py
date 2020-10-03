n = int(input())

a = list(map(int,input().split()))
max_ = a[0]
min_ = a[0]
c_max = 0
c_min = 0
for i in range(1 , n):
    if a[i] > max_:
        c_max += 1
        max_ = a[i]
    elif a[i] == max_:
        pass
    elif a[i] < min_:
        c_min += 1
        min_ = a[i]
    
print(c_max,c_min)