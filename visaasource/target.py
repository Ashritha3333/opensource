t=int(input())
for _ in  range(t):
    x,y=map(int,input().split())
    r=max(0,(x+1)-y)
    print(r)
