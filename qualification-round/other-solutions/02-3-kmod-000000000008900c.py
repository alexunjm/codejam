import sys

def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(b % a, a)

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    T = int(f.readline())
    for _T in xrange(T):
        N, L = map(int, f.readline().split())
        X = map(int, f.readline().split())

        P = [None] * (L + 1)

        for i in xrange(L - 1):
            if X[i] != X[i + 1]:
                break
        else:
            raise Exception(1)

        P[i + 1] = gcd(X[i], X[i + 1])
        P[i] = X[i] / P[i + 1]
        P[i + 2] = X[i + 1] / P[i + 1]

        for j in xrange(i - 1, -1, -1):
            P[j] = X[j] / P[j + 1]
        for j in xrange(i + 1, L):
            P[j + 1] = X[j] / P[j]

        assert all(P)

        primeset = sorted(set(P))

        ans = []
        for p in P:
            ans.append(chr(ord('A') + primeset.index(p)))
        ans = ''.join(ans)

        print "Case #%d: %s" % (_T + 1, ans)
