num=[]
pos=[]
neg=[]
zero=[]
print("Enter 5 numbers:")
for x in range(0,5):
    ip=int(input())
    num.append(ip)

for y in range(0,5):
    if int((num[y]>0)):
        pos.append(num[y])
    elif int((num[y]<0)):
        neg.append(num[y])
    else:
        zero.append(num[y])
print(pos)
print(neg)
print(zero)