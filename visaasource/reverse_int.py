def rev(n):
    int_min,int_max=-2**31,2**31
    sign=-1 if n<0 else 1
    ren=int(str(abs(n))[::-1])*sign
    if ren<int_min or ren>int_max:
        return 0
    return ren
n=int(input().strip())
print(rev(n))
