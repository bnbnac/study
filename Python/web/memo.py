n = int(input())
cnt = 0

while n != 1:
    if n % 3 == 0:
        n //= 3
        cnt += 1
    elif n % 3 == 1:
        n -= 1
        cnt += 1

    elif n % 6 == 2:
        n // 2
        cnt += 1
    elif n % 6 == 5:
        n -= 1
        cnt += 1

print(cnt)