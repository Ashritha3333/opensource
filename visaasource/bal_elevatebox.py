def cal(n,a):
    tot=sum(a)
    bal=[]
    l=0
    for i in range(n):
        r=tot-l-a[i]
        val=abs(l-r)
        bal.append(val)
        l+=a[i]
    return bal
n=int(input())
a=list(map(int,input().split()))
r=cal(n,a)
print(" ".join(map(str,r)))
