t = int(input())

def solve():
    n = int(input())
    p = input()
    result = ""
    
    for index in range(len(p)):
        if p[index] == "S":
            result += "E"
        else:
            result += "S"
            
    # return "{}".format(result)
    return result
            
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, solve()))