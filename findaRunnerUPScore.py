n = int(input())
arr = list(map(int, input().split()))

blank = []



for i in arr:
    if i not in blank:
        blank.append(i)

max_ = max(blank)
blank.remove(max_)
print(max(blank))