n = int(input())
l = []
for i in range (n):
    score = int(input())
    l.append(score)
for i in l:
    if i%5>2 and i>37:
        i += 5 - (i%5)
        print(i)
    else:
        i = i
        print(i)
