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
s = data[2]
edges = [[] for _ in range(n)]
idx = 3
for _ in range(m):
    a = int(data[idx]) - 1
    b = int(data[idx + 1]) - 1
    idx += 2
    edges[a].append(b)
    edges[b].append(a)


# 1. first find the number of connected components
# 2. find the frequency of each word while you are doing the dfs
def dfs(x, frequency, visited):
    visited[x] = True
    frequency[s[x]] = frequency.get(s[x], 0) + 1
    num_nodes = 1
    for nbr in edges[x]:
        if not visited[nbr]:
            num_nodes += dfs(nbr, frequency, visited)
    return num_nodes



PRIME_MOD = 998244353
fact = [1 for _ in range(n + 1)]
for i in range(1, n + 1):
    fact[i] = (fact[i - 1] * i) % PRIME_MOD

total = 1
visited = [False for i in range(n)]
single_count = True
for i in range(n):
    if not visited[i]:
        frequency = {}
        num_nodes = dfs(i, frequency, visited)
        count = fact[num_nodes]
        for letter in frequency:
            count = (count * pow(fact[frequency[letter]], PRIME_MOD - 2, PRIME_MOD)) % PRIME_MOD
            # count = count // fact[frequency[letter]]
            if frequency[letter] > 1:
                single_count = False

        total = (total * count) % PRIME_MOD

if single_count:
    total = (total * pow(2, PRIME_MOD - 2, PRIME_MOD)) % PRIME_MOD

print(total)



