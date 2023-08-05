def armstrong(n):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print(num," is a Armstrong number ")
    else:
        print(num,"is not an Armstrong number")
num=int(input("Enter num: "))
armstrong(num)

def ispalindrome(s):
    return s==s[::-1]

s=input("Enter a String: " )
ans=ispalindrome(s)

if ans:
    print(s," is palindrome")
else:
    print(s, " is not palindrome")
