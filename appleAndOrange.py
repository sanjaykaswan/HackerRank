s,t = map(int,input().split())
a,b = map(int,input().split())
m,n = map(int,input().split())
app = list(map(int,input().split()))
orng = list(map(int,input().split()))
x = 0
y = 0
for i in app:
    if t-a>= i >=s-a:
        x += 1
for c in orng:
    if t-b>= c >= s-b:
        y += 1
print(x)
print(y)