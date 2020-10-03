import sys
import re
p = re.compile(r'(?<=\w)([\$\#\%\s]+)(?=\w)')
inp = sys.stdin.readline().split();
r = int(inp[0])
c = int(inp[1])
rows = [l for l in sys.stdin]
answer = ""
for i in range(c):
    for j in range(r):
        answer += rows[j][i]
print(p.sub(' ',answer))