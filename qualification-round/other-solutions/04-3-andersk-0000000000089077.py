from math import gcd
import string

t = int(input())
for x in range(1, t + 1):
    n, l = map(int, input().split())
    *c, = map(int, input().split())
    i = next(i for i, k in enumerate(c) if k != c[0])
    g = gcd(c[0], c[i])
    p = (i + 1) % 2 * [g] + (i + 1) // 2 * [c[0] // g, g]
    for k in c[i:]:
        g = k // g
        p.append(g)
    decode = dict(zip(sorted(set(p)), string.ascii_uppercase))
    y = "".join(decode[k] for k in p)
    print("Case #{}: {}".format(x, y))