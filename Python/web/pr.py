bef = []
aft = []

diff = []

n, m = map(int, input().split())
for i in range(n):
    bef.append([])
    ithbef = input()
    for j in range(m):
        bef[i].append(int(ithbef[j]))
print(bef)
for i in range(n):
    aft.append([])
    ithaft = input()
    for j in range(m):
        aft[i].append(int(ithaft[j]))

for i in range(n):
    diff.append([])
    for j in range(m):
        diff[i][j] = bef[i][j] + aft[i][j]
        diff[i][j] %= 2
print(diff)
def stamp(Matrix, x, y): ## input center coordi, stamp 3x3 with bullian
    for i in range(3):
        for j in range(3):
            Matrix[x - 1 + i][y - 1 + j] += 1
            Matrix[x - 1 + i][y - 1 + j] %= 2


#def transable(Matrix, x, y):
    # 