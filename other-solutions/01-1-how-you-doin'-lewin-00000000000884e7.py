t = int(input())

def solve():
    s = input()
    a = ""
    for i in range(len(s)):
        if s[i] == '4':
            a += '1'
        else:
            a += '0'
    return "%s %s" % (int(a), int(s)-int(a))

    
for __ in range(t):
    print ("Case #%d: %s" % (__+1, solve()))