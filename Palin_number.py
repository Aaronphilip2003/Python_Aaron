num=int(input("Enter a number:"))
temp=num
rev=0
r=0
while num>0:
    r=num%10
    rev=rev*10+r
    num//=10
if rev==temp:
    print("Palin")
else:
    print("NOT")

