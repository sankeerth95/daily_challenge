import sys
from bisect import bisect_right
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

idx = 0
T = int(data[idx])
idx = idx + 1
for t in range(T):
    n = int(data[idx])
    idx = idx + 1

    x = int(data[idx])
    idx = idx + 1

    a = [ int(data[idx+i]) for i in range(n) ]
    idx = idx + n

    # a_filt strictly decreasing.
    a_filt = [x + 1]
    for value in a:
        if value < a_filt[-1]:
            a_filt.append(value)

    n_filt = len(a_filt)

    # print(a_filt)

    #######################################################################
    # loop backwards and 
    limit = a_filt[n_filt-1]
    minlimit = a_filt[n_filt-1]
    running_count = 1
    countlimitinclusive = {limit: running_count}
    sorted_limits = [limit]
    for i in range(n_filt-1):
        factor = a_filt[n_filt-i-2] // a_filt[n_filt-i-1]
        remainder = a_filt[n_filt-i-2] % a_filt[n_filt-i-1]

        residual = 0
        while remainder >= minlimit:
            remainder_limit = get_limit(remainder, sorted_limits)
            remainder_running_count = countlimitinclusive[remainder_limit]
            residual += (remainder // remainder_limit) * remainder_running_count
            remainder = remainder % remainder_limit

        # If a non-empty tail remains, it contains 0, which always finishes at
        # 0 after any number of modulo operations.
        if remainder > 0:
            residual += 1

        running_count = running_count * factor + residual
        limit = a_filt[n_filt-i-2]
        countlimitinclusive[limit] = running_count
        sorted_limits.append(limit)

    # The interval [0, X + 1) includes 0, while the problem asks for [1, X].
    print(countlimitinclusive[x + 1] - 1)




