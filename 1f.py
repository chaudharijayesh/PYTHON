def facto(x):
    if x==1:
        return 1
    else:
        return (x*facto(x-1))

n=int(input("Enter : "))
result=facto(n)
print("factorial of "+str(n)+" is "+str(result))