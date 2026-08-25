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
q = int(data[1])
idx = 2
x = [[] for _ in range(n)]
y = [[] for _ in range(n)]
for i in range(n):
    x[i], y[i] = int(data[idx]), int(data[idx+1])
    idx += 2


center = [0, 0]
for i in range(n):
    center[0] += x[i]
    center[1] += y[i]

# Keep n * center as integers instead of dividing here.
def get_signed_area(i, j):
    # This is n times the doubled signed area of triangle center, i, j.
    return (
        n * (x[i] * y[j] - x[j] * y[i])
        + center[0] * (y[i] - y[j])
        + center[1] * (x[j] - x[i])
    )


def get_centroid(i, j):
    # These are 3n times the triangle centroid coordinates.
    return (
        n * (x[i] + x[j]) + center[0],
        n * (y[i] + y[j]) + center[1],
    )


class GetSum:
    def __init__(self, data):
        # construct cumulative sum structure
        self.csum = [0]
        for d in data:
            self.csum.append(self.csum[-1] + d)

    # sum of i, i+1, ... j-1
    # wrapped sum if i > j
    def get_sum(self, i, j):
        if i < j:
            return self.csum[j] - self.csum[i]
        elif i == j:
            return 0
        else:
            return self.csum[-1] - self.csum[i] + self.csum[j]


centroids = [get_centroid(i, (i + 1) % n) for i in range(n)]
areas = [get_signed_area(i, (i + 1) % n) for i in range(n)]
weighted_centroids_X = [areas[i] * centroids[i][0] for i in range(n)]
weighted_centroids_Y = [areas[i] * centroids[i][1] for i in range(n)]

weighted_centroid_x_sum = GetSum(weighted_centroids_X)
weighted_centroid_y_sum = GetSum(weighted_centroids_Y)
area_sum = GetSum(areas)

for _ in range(q):
    u, v = int(data[idx]), int(data[idx+1])
    idx += 2

    u -= 1
    v -= 1

    area_uv = get_signed_area(u, v)
    centroid_uv = get_centroid(u, v)
    num_x = weighted_centroid_x_sum.get_sum(u, v) - area_uv * centroid_uv[0]
    num_y = weighted_centroid_y_sum.get_sum(u, v) - area_uv * centroid_uv[1]
    denom = area_sum.get_sum(u, v) - area_uv

    ans = (num_x / (3 * n * denom), num_y / (3 * n * denom))
    print(ans[0], ans[1])




