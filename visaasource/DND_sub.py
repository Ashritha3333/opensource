def num(n,m):
    n1=n2=0
    for a in n:
        if a%m!=0:
            n1+=a
        else:
            n2+=a
    return (n2-n1)
f=input().split()
n=int(f[0])
m=int(f[1])
arr=list(map(int,input().split()))

print(num(arr,m))
