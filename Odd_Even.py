numbers=[]
odd=[]
even=[]
print("Enter 5 numbers:")
for x in range(0,5)  :
    inp=int(input())
    numbers.append(inp)

for y in range(0,5):
    if int(numbers[y]%2==0):
        odd.append(numbers[y])
    elif int(numbers[y]%2!=0):
        even.append(numbers[y])


print(odd)
print(even)