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
m = int(data[1])
a = [ [] for _ in range(n)]
b = [ [] for _ in range(n-1)] 
idx=2
for i in range(n):
    a[i] = int(data[idx])
    idx += 1

for i in range(n-1):
    b[i] = int(data[idx])
    idx += 1



r = [ [] for _ in range(n-1) ]
for i in range(n-1):
    r[i] = (2*m - a[i] - a[i+1] + b[i]) % m


incr = [ [] for i in range(n) ]
incr[0] = (0, 0)
for i in range(1, n):
    incr[i] =  ( ((2*m + r[i-1] - incr[i-1][0]) % m) , i )

incr.sort()
count = 0
for x in incr:
    count += x[0]

mincount = count
for i in range(1, n):
    if n % 2 == 1:
        count += incr[i][0] - incr[i-1][0]

    if incr[i][1]%2 == 1: # hit a minus position boundary
        mincount = min(count, mincount)
        count += m
    else:           # hit a plus position
        count -= m
        mincount = min(count, mincount)

print(mincount)



