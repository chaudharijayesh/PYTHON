num=int(input("Enter a range "))
i=1
a=0
b=1
c=0
print("Fabonacci series: ", end="")
while i<=num :
    print(a, end= " ")
    i+=1
    c=a+b
    a=b
    b=c



