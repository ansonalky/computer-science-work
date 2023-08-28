# hour of code #24
Numberlist=[0 for __ in range(0,10)]
for n in range(0,10):
    Numberlist[n]=0
number=int(input("Enter numbers:"))
while number!=0:
    Numberlist[number-1]=Numberlist[number-1]+1
    number=int(input("Enter numbers:"))
print(Numberlist)