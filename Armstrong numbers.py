def count (n)
c=0
while(n!==0):
    n//10
    c=c+1
    return(c)
x=153
n=153
s=0
c=count(n)
while(n):
    a=n%10
    n=n//10
    if(x==s):
        print("armstromg number")
    else:
        print("not armstrong")
