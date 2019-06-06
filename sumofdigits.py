n=int(input("Enter integer: "))
sum=0
while n>0:
    d=int(n%10)
    n=n/10
    sum=sum+d

print("Sum of digits of integer is: ",sum)
