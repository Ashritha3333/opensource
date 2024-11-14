a=int(input())
r=[]
for _ in range(a):
    n,m=map(int,input().split())
    r.append(max(0,n-m))
print("\n".join(map(str,r)))
