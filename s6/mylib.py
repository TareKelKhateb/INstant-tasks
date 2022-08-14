def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac

def sum_list(l):
    sum=0
    for i in range l:
        sum+=i
    return sum