M = [2000,500,200,100,50,20,10,5,2,1]

#n = int(input())
n=int(input())

i=0
sum=0
while(i<10):
    if M[i] > n: # 2000 > 2031 false 2000 > 31 true
        i+=1
    else:
        sum+=1 # 
        n-=M[i] #2031-2000 = 31

print(sum)