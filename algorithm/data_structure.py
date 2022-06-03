from collections import deque
import sys
input = sys.stdin.readline

queue = deque([])
n = int(input())
for i in range(n):
    oper = list(input().split())
    try:
        if len(oper)==2:
            queue.append(oper[1])
        elif oper[0] == "pop":
            print(queue.popleft())
        elif oper[0] == "size":
            print(len(queue))
        elif oper[0] == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif oper[0] == "front":
            print(queue[0])
        else:
            print(queue[-1])
    except:
        print(-1)