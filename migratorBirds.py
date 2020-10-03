n = int(input())

num = list(map(int,input().split()))

print(max(set(num),key = num.count))