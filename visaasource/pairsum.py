n=int(input())
arr=list(map(int,input().split()))
k=int(input())
seen=set()
f=False
for num in arr:
    c=k-num
    if c in seen:
        f=True
        break
    seen.add(num)
print("true" if f else "false")
