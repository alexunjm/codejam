
from fractions import gcd

def solve():
    trash,n=map(int,raw_input().split())
    a = map(int,raw_input().split())
    assert len(a)==n

    z = [-1 for _ in range(n+1)]
    for i in range(1,n):
        x,y=a[i-1],a[i]
        if x==y:
            continue
        z[i]=gcd(x,y)

        for j in range(i)[::-1]:
            assert a[j]%z[j+1] == 0
            z[j] = a[j]/z[j+1]
        for j in range(i+1,n+1):
            assert a[j-1]%z[j-1]==0
            z[j] = a[j-1]/z[j-1]

        zz=sorted(list(set(z)))
        assert len(zz)==26

        def idx(x):
            for i in range(26):
                if zz[i]==x:
                    return chr(ord('A')+i)
            assert False
        return ''.join(map(idx,z))

    assert False




T=input()
for t in range(T):
    print ("Case #%s:" % (t+1)),
    print solve()


