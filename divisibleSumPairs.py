n, k = map(int,input().split())

num = list(map(int,input().split()))

c = 0

for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            if (num[i]+num[j])%k == 0:
                c+=1
print(c//2)