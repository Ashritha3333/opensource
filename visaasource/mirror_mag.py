n=int(input())
m=[]
for _ in range(n):
    r=list(map(int,input().split()))
    m.append(r)
mm=[r[::-1] for r in m]
for r in mm:
    print(" ".join(map(str,r)))
    
