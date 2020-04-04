t = int(input())
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def isPrime(n):
    middle = 0
    if n % 2 == 0:
        middle = n // 2
    else:
        middle = (n - 1) // 2
    for i in range(middle, 1, -1):
        if n % i == 0:
            return False
    # print("primo: {}".format(n))
    return True

arr = []
def primeArr(n):

    start = 3
    arrLen = len(arr)
    if arrLen > 0:
        start = arr[arrLen - 1] + 1
    for num in range(start, n + 1):
        if isPrime(num):
            arr.append(num)
    return arr

def solve():
    n, l = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    pangram = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    # print(len(pangram))
    return primeArr(n)
            
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, solve()))