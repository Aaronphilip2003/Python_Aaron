num=int(input("Enter a number:"))
temp=num
pro=1
r=0
while num>0:
    r=num%10
    pro*=r
    num//=10
if(pro==0):
    print("DUCK")
else:
    print("NOT")

