n, m=map(int,input().split())
def game(n, m):
    a = 0
    b = 0
    if n%2 == 0:
        a = n//2
    else:
        a = n//2 +1
    if m%2 == 0:
        b = m//2
    else:
        b = m//2 +1
    return print(a*b)

game(n, m)