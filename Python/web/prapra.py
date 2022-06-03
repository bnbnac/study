n = int(input())
num = list(map(int, input().split()))
num.sort(reverse=True)

for p in range(1, 9999999):
    numt = []
    for i in range(n):
        numt.append(num[i])
    pp = p
    while len(numt) != 0:
        if numt[0] > pp:
            del numt[0]
        else:
            lar = numt[0]
            del numt[0]
            pp = pp - lar
            if pp == 0:
                break   
    if len(numt) == 0 and pp != 0:
        print(p)         
        break
