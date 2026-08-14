
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
p = [int(data[i]) for i in range(1, n + 1)]



# max sequence length
max_seq_len = 0
reduced_seq = []
max_now = 0
for i in range(len(p)):
    if p[i] > max_now:
        max_now = p[i]
        max_seq_len += 1
    else:
        reduced_seq.append(i)

# remove the max_seq indieces from p
p_red = [p[i] for i in reduced_seq]

def lis(p):
    def get_idx(arr, x):
        # gets max index where arr[idx] < x in sorted array arr
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left

    tails = []
    for x in p:
        idx = get_idx(tails, x)
        if idx >= len(tails):
            tails.append(x)        
        else:
            tails[idx] = x
#        print(idx, tails)
    return len(tails)

min_seq_len = lis(p_red)
print(min_seq_len + max_seq_len)


