def check(s):
    if (s[-1]=='e'):
        return False
    if s[0]=='-':
        s=s[1:]
    for i in s:
        if (i in '1234567890') or (i=='e' or i=='.'):
                pass
        else:
            return False
    return True

s=input()
print(check(s))

# using inbuilt function
# try:
#     eval(s)
#     result = True
# except:
#     result = False    
# print(result)