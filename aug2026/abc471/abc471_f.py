import sys
from bisect import bisect_right
from functools import cmp_to_key
sys.setrecursionlimit(10**7)


def read_tokens():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            tokens = f.read().split()
    else:
        tokens = sys.stdin.buffer.read().split()
    return [t.decode() if isinstance(t, bytes) else t for t in tokens]


def get_limit(target, sorted_keys):
    idx = bisect_right(sorted_keys, target) - 1
    if idx < 0:
        return 0
    return sorted_keys[idx]


data = read_tokens()
if not data:
    raise SystemExit

n = int(data[0])
k = int(data[1])
s = [[] for _ in range(n)]
for i in range(n):
    s[i] = data[2+i]

# get_lead
def get_num_lead_zeros(s):
    cnt = 0
    for ch in s:
        if ch == '0':
            cnt += 1
        else:
            break
    return cnt

# number of diigts not including initial zero
def get_num_digits_nonleadingzero(s):
    return max(0, len(s) - get_num_lead_zeros(s))

# sort s_filt by the number of digits (including leading-zero lengths). if digits are equal then int(s_filt[i]), int(s_filt[j]);
def compare_fn(a, b):
    da = len(a)
    db = len(b)
    if da != db:
        return -1 if da > db else 1
    va = int(a)
    vb = int(b)
    if va != vb:
        return -1 if va > vb else 1
    return 0

# sorting logic with compare_fn
s.sort(key=cmp_to_key(compare_fn))

# print(s)

max_lead_number_outside = 0
for j in range(k, n):
    if max_lead_number_outside < int(s[j]):
        max_lead_number_outside = int(s[j])
ans1 = str(max_lead_number_outside) + ''.join(s[:k-1])



max_lead_number_within = "0"
max_lead_number_within_idx = 0
for j in range(k):
    # compare x with max_lead_digit: 
    ## iterate through the nonzero digits of s
    nonzero_portion = False
    i = 0
    for c in s[j]:
        if c != "0":
            nonzero_portion = True
        if nonzero_portion:
            if i >= len(max_lead_number_within):
                break
            if int(max_lead_number_within[i]) < int(c):
                max_lead_number_within = s[j]
                max_lead_number_within_idx = j
                break
            i += 1

print(max_lead_number_within_idx)

# move max_lead_number_idx to the first position and shift the previous front elements rightward
# e.g. [a, b, c, d] with idx=2 -> [c, a, b, d]
if max_lead_number_within_idx > 0:
    max_item = s.pop(max_lead_number_within_idx)
    s.insert(0, max_item)

# select first k and concatenate
ans2 = ''.join(s[:k])

ans = str(max(int(ans1), int(ans2)))
print(ans)
# print(ans1, ans2)



