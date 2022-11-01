def isSum(n):
    s=0
    while(n!=0):
        r=n%10
        s+=r*r
        n//=10
    return s

def isHappy(n):
    while(True):
        n=isSum(n)
        if n==1 or n==7:
            return True
        if n<10:
            return False
n=int(input())
print(isHappy(n))
