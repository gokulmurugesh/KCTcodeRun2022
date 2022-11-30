a,b,c = int(input()),int(input()),int(input())

def min(x,y):
    
    if((x ^ y) >> 31): #opposite sign, logic : (xor) (shift - 32bit int)
        return x if ((x^1) >> 31) else y #return negative
    
    else: #same sign
        if((x ^ -1) >> 31) and ((y ^ -1) >> 31): #x and y are positive note: doesn't need to evaluate both
            return y if (x//y) else x #if x/y is positive, then y is small
    
        if((x ^ 1) >> 31) and ((y ^ 1) >> 31): #x and y are negative
            return x if(x//y) else y #if x/y is postive, then x is small


print(min(a,min(b,c)))

# postive numbers only
# def min(x,y):
#     return y if (x//y) else x
# min(5,6)

# with inbuilt function
# l = [a,b,c]
# print(min(l))
