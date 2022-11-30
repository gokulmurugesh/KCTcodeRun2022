def fun(n):
    e=0
    while(n!=1):
        if(n%2 == 0):
            n=n/2
            e+=1
        else:
            return "not a power of 2"
    return "2^"+str(e)

n=int(input())
print(fun(n))