n = int(input())
uid_list = []
for i in range(1,n+1):
    uid = input()
    uid_list.append(uid)



alpha = '''abcdefghijklmnopqrstuvwxyz'''
Alpha = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
numeric = '0123456789'
N = 0
A = 0
a = 0
valid = []
rep = 0

for i in uid_list:
    for j in i:
            if j in Alpha:
                A += 1
            elif j in numeric:
                N += 1
            elif j in alpha:
                a += 1
            if j not in valid:
                valid.append(j)
            elif j in valid:
                rep += 1
            

    
    

    if A>=2 and N>=3 and len(i)==10 and a + A + N == 10 and rep==0:
        print('Valid')
    else:
        print('Invalid')
    A = 0
    N = 0
    a = 0
    rep = 0
    valid.clear()