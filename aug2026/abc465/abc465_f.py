import sys
sys.setrecursionlimit(10**7)

def read_tokens():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            tokens = f.read().split()
    else:
        tokens = sys.stdin.buffer.read().split()
    return [t.decode() if isinstance(t, bytes) else t for t in tokens]


data = read_tokens()
if not data:
    raise SystemExit

n = int(data[0])
sv = {}
idx=1
for i in range(n):
    s, v = data[idx], int(data[idx+1])
    idx += 2
    sv[str(s)] = v


# qsum[11][11][11][11][11][11] in C++
M = 11
qsum = [[[[[[0 for _ in range(M)] for _ in range(M)]
                     for _ in range(M)] for _ in range(M)]
                 for _ in range(M)] for _ in range(M)]
for sm in range(6, 61):
    for i0 in range(1, 11):
        for i1 in range(1, 11):
            for i2 in range(1, 11):
                for i3 in range(1, 11):
                    for i4 in range(1, 11):
                        i5 = sm -i0-i1-i2-i3-i4

                        if i5 < 1 or i5 > 10:
                            continue

                        tot = 0
                        for a0 in range(2):
                            for a1 in range(2):
                                for a2 in range(2):
                                    for a3 in range(2):
                                        for a4 in range(2):
                                            for a5 in range(2):
                                                sign = -1 * (2*a0-1)*(2*a1-1)*(2*a2-1)*(2*a3-1)*(2*a4-1)*(2*a5-1)
                                                tot +=  sign * qsum[i0 - a0][i1 - a1][i2 - a2][i3 - a3][i4 - a4][i5 - a5] 


                        idx_s = str(i0-1) + str(i1-1) + str(i2-1) + str(i3-1) + str(i4-1) + str(i5-1)
                        qsum[i0][i1][i2][i3][i4][i5] = tot + sv.get(idx_s, 0)
                        
q = int(data[idx])
idx+=1

for q_ in range(q):
    x, y = data[idx], data[idx+1] # string input
    idx += 2 

    if x > y:
        print(0)
        continue

    u = [[], []]
    u[0] = [int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5])]
    u[1] = [int(y[0]), int(y[1]), int(y[2]), int(y[3]), int(y[4]), int(y[5])]
    # post process
    u[1] = [x+1 for x in u[1]]

    # inclusion_exclusion_rountine
    ans = 0
    for a0 in range(2):
        for a1 in range(2):
            for a2 in range(2):
                for a3 in range(2):
                    for a4 in range(2):
                        for a5 in range(2):
                            sign = (2*a0-1)*(2*a1-1)*(2*a2-1)*(2*a3-1)*(2*a4-1)*(2*a5-1)
                            ans += sign * qsum[u[a0][0]][u[a1][1]][u[a2][2]][u[a3][3]][u[a4][4]][u[a5][5]]

    print(ans)


