def rotate(n,arr):
    s=arr[1:]+arr[:1]
    return s
n=int(input())
arr=list(map(int,input().split()))
a=rotate(n,arr)
print(" ".join(map(str,a)))
