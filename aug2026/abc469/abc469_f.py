
import sys
from itertools import combinations

sys.setrecursionlimit(10**7)


def read_tokens():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            tokens = f.read().split()
    else:
        tokens = sys.stdin.buffer.read().split()
    return [t.decode() if isinstance(t, bytes) else t for t in tokens]


class unionfind:
    def __init__(self, values):
        self.parent = {value: value for value in values}
        self.size = {value: 1 for value in values}
        self.components = len(self.parent)

    def root(self, value):
        if self.parent[value] != value:
            self.parent[value] = self.root(self.parent[value])
        return self.parent[value]

    def union(self, first, second):
        first_root = self.root(first)
        second_root = self.root(second)
        if first_root == second_root:
            return

        if self.size[first_root] < self.size[second_root]:
            first_root, second_root = second_root, first_root

        self.parent[second_root] = first_root
        self.size[first_root] += self.size[second_root]
        self.components -= 1

    def numclusters(self):
        return self.components


data = read_tokens()
if not data:
    raise SystemExit

n = int(data[0])
a = [int(data[i]) for i in range(1, n + 1)]
max_a = max(a)


def solve():
    index_of = [-1] * (max_a + 1)
    for index, value in enumerate(a):
        index_of[value] = index

    ans = 0
    clusters = unionfind(range(n))

    for i in range(max_a, 0, -1):
        dividing_node = -1
        for multiple in range(i, max_a + 1, i):
            a_idx = index_of[multiple]
            if a_idx == -1:
                continue
            if dividing_node == -1:
                dividing_node = a_idx
            elif clusters.root(dividing_node) != clusters.root(a_idx):
                clusters.union(dividing_node, a_idx)
                ans += i

                if clusters.numclusters() == 1:
                    return ans

    return ans


print(solve())
