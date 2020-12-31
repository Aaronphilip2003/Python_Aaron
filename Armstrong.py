#153=1^3+5^3+3^3
num=int(input("Enter a number:"))
sum=0
temp=num
while num>0:
    r=int(num%10)
    sum+=r*r*r
    num=num//10
if sum==temp:
    print("Armstrong")
else:
    print("NOT")
