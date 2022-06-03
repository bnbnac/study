from collections import deque
import sys
import queue
input = sys.stdin.readline
num = int(input())
seq = deque([])
paper = []
for i in range(num):
    seq.append(int(input()))

between = 0
last = 0
count = 0
while len(seq) > 0:
    next = seq.popleft()
    diff = next - last
    if diff > 0:
        for _ in range(count):
            paper.append('-')
        for _ in range(diff):
            paper.append('+')
        last = next
        count = 1
    else:
        count += 1
    if next == num:
        paper.append('-')
        break
no = 0
while len(seq) > 0:
    next = seq.popleft()
    if next > last:
        no = 1
        break
    else:
        paper.append('-')
        last = next

if no == 1:
    print("NO")
else:
    for p in paper:
        print(p)