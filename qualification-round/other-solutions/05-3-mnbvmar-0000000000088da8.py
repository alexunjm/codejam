#!/usr/bin/env python3

import math

T = int(input())

for tidx in range(1, T + 1):
    n, L = map(int, input().split())
    enc = list(map(int, input().split()))

    diff_loc = -1
    for i in range(L - 1):
        if enc[i] != enc[i + 1]:
            diff_loc = i
            gcd = math.gcd(enc[i], enc[i + 1])
            break

    assert(diff_loc != -1)
    
    mid_dec = [None] * (L + 1)
    mid_dec[diff_loc + 1] = gcd
    mid_dec[diff_loc] = enc[diff_loc] // gcd
    mid_dec[diff_loc + 2] = enc[diff_loc + 1] // gcd
    for i in range(diff_loc - 1, -1, -1):
        mid_dec[i] = enc[i] // mid_dec[i + 1]
    for i in range(diff_loc + 3, L + 1):
        mid_dec[i] = enc[i - 1] // mid_dec[i - 1]

    primes = list(set(mid_dec))
    primes.sort()
    assert(len(primes) == 26)

    alpha_map = dict()

    for i in range(len(primes)):
        alpha_map[primes[i]] = chr(ord('A') + i)

    answer = ''.join([alpha_map[x] for x in mid_dec])

    print("Case #{}: {}".format(tidx, answer))

