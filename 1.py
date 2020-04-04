t = int(input()) # read a line with a single integer

def solve():
    n = input() # read n value
    
    a = ""
    b = ""
    
    for index in range(len(n)):
        if n[index] == "4":
            b += str(int(n[index])-1)
            a += "1"
        else:
            b += n[index]
            a += "0"
            
    return "{} {}".format(b, int(n) - int(b))
            
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, solve()))