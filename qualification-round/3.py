from math import gcd

t = int(input())

def solve():
    n, l = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    arr = input() # read a list of integers, 2 in this case
    crypto = [int(s) for s in arr.split(" ")] # read a list of integers, 2 in this case
    primes = [0] * (l+1)
    for i in range(l):
        if crypto[i] != crypto[i+1]:
            gcdCalc = gcd(crypto[i], crypto[i+1])
            primes[i+1] = gcdCalc
            
            for j in range(i, -1, -1):
                # print("calculating: {} / {}".format(crypto[j], primes[j+1]))
                primes[j] = crypto[j] // primes[j+1]

            # print("crypto: {}".format(crypto))
            for j in range(i+2, l+1):
                # print("primes: {}".format(primes))
                # print("calculating: {} / {}".format(crypto[j-1], primes[j-1]))
                primes[j] = crypto[j-1] // primes[j-1]

            break
    print(primes)
    setOfPrimes = []
    for p in primes:
        if p not in setOfPrimes:
            setOfPrimes.append(p)
    
    setOfPrimes = sorted(setOfPrimes)
    print('setOfPrimes: {}'.format(setOfPrimes))
    res = ''.join([chr(ord('A')+setOfPrimes.index(prime)) for prime in primes])
    return res
            
for i in range(1, t+1):
    print("Case #{}: {}".format(i, solve()))